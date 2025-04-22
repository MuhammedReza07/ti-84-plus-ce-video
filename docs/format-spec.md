# Video File Format Specification
This specification describes the technical details of the **Run-length Encoded Monochrome Video** (RLEMV) file format. RLEMV files shall have the extension `.rlemv`. RLEMV is designed to yield a reasonable amount of compression while still being possible to decode efficiently, making it suitable for applications such as playing monochrome video with limited computational power and memory.

# Background
The RLEMV file format was primarily designed to take into account various aspects of the TI-84 Plus CE's hardware. Some of the aspects that informed the design of the format are listed below.
- The Zilog eZ80 is clocked at 48 MHz and its performance is further degraded by wait states, which means that modern video compression techniques based on expensive mathematical transformations are probably far too expensive to be viable on the TI-84 Plus CE. Additionally, more efficient compression algorithms such as LZ77/LZSS may add additional overhead to the frame decoding process due to periodically needing to decode *entire* chunks of the video before displaying them. This is in contrast to simpler compression algorithms such as run-length encoding that yield displayable pixel data immediately after the number of repetitions has been computed.
- Due to the TI-84 Plus CE only making 3 MB of ROM and 154 KB of RAM accessible to the user, the size of the video is limited to under 3 MB as it must fit in the archive. Furthermore, the limited size of RAM makes it impossible to load the entire video into RAM at once. This necessitates reading the video in chunks, which would have been necessary even without the limit on the amount of RAM (at least if hardcoding frames into the video player is to be avoided) since the maximum size of an application variable (the TI-84 equivalent to a file) is the greatest value that fits in a `uint16_t`.
- The LCD controller of the TI-84 Plus CE has several graphics modes, ranging from 1 bpp (bits per pxel) to 24 bpp (basically RGB colour, which is impossible to use in practice due to the limited size of VRAM). The operating system of the TI-84 Plus CE operates in a 16 bpp graphics mode. Graphics modes with less than 24 bpp operate by treating values written to VRAM as indices into a 256x16 bit RAM palette on the LCD controller. For instance, the 8 bpp graphics mode treats values written to VRAM as 8-bit indices into the palette. If the goal is to display monochrome graphics, the 1 bpp graphics mode is most appropriate as it reduces both file size and the number of writes to VRAM, making encoding and decoding the video more efficient. The trade off here is the the CE C libraries do not provide any functionality for graphics modes other than 8 bpp (which is provided in [`graphx.h`](https://ce-programming.github.io/toolchain/libraries/graphx.html)). Another limitation that is imposed by the requirement of compatibility with the 1 bpp graphics mode is that all encoding and decoding routines must operate on 8-bit blocks. This in turn makes encoding the video column-by-column more efficient than encoding row-by-row. This is because a (320x240) frame contains 40 8-bit blocks in each row but 240 8-bit blocks in each 8-bit wide column of a frame.

# File Structure Summary
RLEMV files are structurally similar to PBMs, differing only in the type and encoding of binary content. A RLEMV file has the following structure.

    RLEMV
    <size: uint64_t>
    <Run-length encoded frame data>

The initial (ASCII encoded) `RLEMV` is the file magic, `size` is a `uint64_t` that consists of two concatenated `uint32_t` values representing the width and height. Specifically, `<size> = <width><height>`, meaning that the field may be treated as two adjacent `uint32_t` values if bit manipulation is to be avoided.

**Note: the line breaks in the description of the RLEMV file format given above were added for clarity only and are not included in actual RLEMV headers.**

# Encoding
TODO

# Decoding
TODO

# Conversion to Application Variables
TODO