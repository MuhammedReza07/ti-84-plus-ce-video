# Video File Format Specification
This specification describes the technical details of the **Run-length Encoded Monochrome Video** (RLEMV) file format. RLEMV files shall have the extension `.rlemv`. RLEMV is designed to yield a reasonable amount of compression while still being possible to decode efficiently, making it suitable for applications such as playing monochrome video with limited computational power and memory.

# Conventions
- All values are little-endian unless stated otherwise, i.e. multi-byte values are stored with the least significant byte first.

# Background
The RLEMV file format was primarily designed to take into account various aspects of the TI-84 Plus CE's hardware. Some of the aspects that informed the design of the format are listed below.
- The Zilog eZ80 is clocked at 48 MHz and its performance is further degraded by wait states, which means that modern video compression techniques based on expensive mathematical transformations are probably far too expensive to be viable on the TI-84 Plus CE. Additionally, more efficient compression algorithms such as LZ77/LZSS may add additional overhead to the frame decoding process due to periodically needing to decode *entire* chunks of the video before displaying them. This is in contrast to simpler compression algorithms such as run-length encoding that yield displayable pixel data immediately after the number of repetitions has been computed.
- Due to the TI-84 Plus CE only making 3 MB of ROM and 154 KB of RAM accessible to the user, the size of the video is limited to under 3 MB as it must fit in the archive. Furthermore, the limited size of RAM makes it impossible to load the entire video into RAM at once. This necessitates reading the video in chunks, which would have been necessary even without the limit on the amount of RAM (at least if hardcoding frames into the video player is to be avoided) since the maximum size of an application variable (the TI-84 equivalent to a file) is the greatest value that fits in a `uint16_t`.
- The LCD controller of the TI-84 Plus CE has several graphics modes, ranging from 1 bpp (bits per pxel) to 24 bpp (basically RGB colour, which is impossible to use in practice due to the limited size of VRAM). The operating system of the TI-84 Plus CE operates in a 16 bpp graphics mode. Graphics modes with less than 24 bpp operate by treating values written to VRAM as indices into a 256x16 bit RAM palette on the LCD controller. For instance, the 8 bpp graphics mode treats values written to VRAM as 8-bit indices into the palette. If the goal is to display monochrome graphics, the 1 bpp graphics mode is most appropriate as it reduces both file size and the number of writes to VRAM, making encoding and decoding the video more efficient. The trade off here is the the CE C libraries do not provide any functionality for graphics modes other than 8 bpp (which is provided in [`graphx.h`](https://ce-programming.github.io/toolchain/libraries/graphx.html)). Another limitation that is imposed by the requirement of compatibility with the 1 bpp graphics mode is that all encoding and decoding routines must operate on 8-bit blocks. This in turn makes encoding the video column-by-column more efficient than encoding row-by-row. This is because a (320x240) frame contains 40 8-bit blocks in each row but 240 8-bit blocks in each 8-bit wide column of a frame.

# File Structure Summary
RLEMV files are structurally similar to PBMs, differing only in the type and encoding of binary content. A RLEMV file has the following structure.

    RLEMV
    <size: uint64_t>
    <frame rate: uint8_t>
    <Run-length encoded frame data>

The initial (ASCII encoded) `RLEMV` is the file magic, `size` is a `uint64_t` that consists of two concatenated `uint32_t` values representing the width and height. Specifically, `<size> = <width><height>`, meaning that the field may be treated as two adjacent `uint32_t` values if bit manipulation is to be avoided. As the name suggests, `<frame rate>` is the frame rate of the encoded video.

**Note: the line breaks in the description of the RLEMV file format given above were only added for clarity and are not included in actual RLEMV headers.**

# Encoding
This section contains an overview of the RLEMV encoding process and some details of the RLEMV encoder implementation used in the video encoding utility.

## RLEMV Video Encoding Overview
The RLEMV video encoding is based on converting the bit stream constituting a monochrome (1 bpp) video into individual frames and applying run-length encoding (RLE) to each frame. What makes RLEMV different from plain RLE is that the encoding is done over the 8 pixel wide columns of each frame, rather than the frame's rows. It is thus possible to encode an entire video by applying an appropriate RLEMV encoding routine to each frame individually and concatenating the results to form a `.rlemv` file (which must contain the appropriate file magic and size). As with other forms of run-length encoding, the RLEMV RLE is basied on converting a sequence of bytes to a sequence of run-length, value pairs. In RLEMV, each such pair takes the form of a `uint16_t`, i.e. two bytes, encoding the data as follows: `<RLE pair> = <run-length><value>`, where `<run-length>` and `<value>` are both one byte. As an example, the 8 pixel sequence

    black black black white white white black white

is encoded as `0b00011101` in a 1 bpp bitmap and a run of 7 such sequences would be converted to `0b00000111 0b00011101` after applying RLE. As runs of length zero should not be generated by the RLE encoder under usual circumstances. Thus the sequence `0b00000000 0b00000000` is used to indicate the end of a frame in RLEMV. This is to facilitate decoding a frame, as checking whether `<run-length>` is `0b00000000` is likely less expensive than keeping track of sums of run-lengths and comparing them with `<size>` to determine whether the end of a frame has been reached. The structure of a single frame thus

    <frame> = <RLE pair><RLE pair> ... <RLE pair> 0b000000000 b00000000

and `<Run-length encoded frame data> = <frame><frame> ... <frame>`.

## Implementation Details
In order to apply RLEMV to a monochrome video provided as e.g. an MP4 file, the frames of the video must be extracted, which may be done using FFmpeg. FFmpeg may also be used to preprocess the video in order to ensure that the resulting video has the desired dimensions and frame rate (which is especially relevant when playing the video on the TI-84 Plus CE). RLEMV is a rather simple format, so the implementation of the encoder in [/convert](../convert/) basically consists of the following components.
- A preprocessing script for video resizing and resampling ([/convert/preprocess-video.sh](../convert/preprocess-video.sh)).
- A RLEMV conversion script ([/convert/rlemv.sh](../convert/rlemv.sh)).

The RLEMV conversion script does the following.
1. Extract the frames of a video and output them as a sequence of PBM files using FFmpeg.
2. Transpose the frames of the video, i.e. reorder the bytes such that pixel data is read in 8-bit columns (INSERT FILE LINK).
3. Run-length encode the transposed frames (INSERT FILE LINK).

# Conversion to Application Variables
TODO