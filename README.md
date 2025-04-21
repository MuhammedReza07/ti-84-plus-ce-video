# Monochrome Video Player for the TI-84 Plus CE

**By Lukas Broström and Muhammed Reza Mehdi<br>**
**DD1349, Group Project**

> **Rule 86:** If it exists, you can play *Bad Apple* on it<br>- *The Rules of the Internet*

For the reader who is not familiar with the TI-84 Plus CE, it is a graphing calculator manufactured by Texas Instruments as part of the TI-84 series of graphing calculators. The TI-84 Plus CE comes with some (for a calculator) surprisingly powerful hardware: it has a 24-bit Zilog eZ80 processor clocked at 48 MHz (true speed severely limited by wait states), 256 KB of RAM (154 KB user-accessible) and 4 MB of ROM (3 MB user accessible). For more information, see the [hardware overview on Cemetech](https://dev.cemetech.net/tools/ti84pce). As for the display, it is a 320x240 colour LCD with support for 16-bit colour, but the LCD controller (an [Arm PrimeCell PL111](https://developer.arm.com/documentation/ddi0293/c?lang=en)) supports more colour modes including a 1 bpp mode for reduced RAM usage (which is excellent for a monochrome video player). Since the TI-84 Plus CE has a display capable of showing at least two colours, the calculator should theoretically be capable of playing monochrome video, such as *Bad Apple* ([link to original video on Nicovideo](https://www.nicovideo.jp/watch/sm8628149)), making playing *Bad Apple* on the calculator the end goal of this project (which hopefully is achievable in about three weeks, otherwise a terminal player will do).

# Goals
- Develop a video encoding utility capable of compressing (low FPS) monochrome video to a size that fits on the TI-84 Plus CE.
- Develop a monochrome video player capable of decoding and displaying video encoded in the developed format.
- Play *Bad Apple* on a TI-84 Plus CE or, if all else fails, the terminal.

# Dependencies
The video player for the TI-84 Plus CE is built using [CE C/C++ Toolchain](https://github.com/CE-Programming/toolchain) and requires the [CE C libraries](https://github.com/CE-Programming/libraries/releases) to run on the calculator or an emulator such as [CEmu](https://github.com/CE-Programming/CEmu). Note that this means that the CE C libraries must be transferred to the calculator prior to running the video player, which may be done using the TI Connect CE software provided by TI. Note also that the video player cannot run on TI-84 Plus CEs with OS version > 5.4.0 as OS versions 5.5.0 and up remove the ability to natively execute assembly code on the TI-84 Plus CE (at least without jailbreaking the calculator).

The video conversion depends on [FFmpeg](https://www.ffmpeg.org/) for converting the video to a format suitable for playing on the TI-84 Plus CE (i.e. low-FPS, 320x240) and for converting the frames of the video to 1 bpp monochrome bitmaps (PBM images to be precise). These images are then processed by a series of C programs that depend on the system's C standard library and `libnetpbm` for processing the bitmaps produced by FFmpeg.

# Build Instructions
For a detailed overview of how to build the video player, the reader is referred to the [CE C/C++ Toolchain documentation](https://ce-programming.github.io/toolchain/static/getting-started.html). 

Building the constituent programs of the video conversion utility may be done using your C/C++ compiler of choice, the only real requirement is linking `libnetpbm` when compiling `transpose-frames.c`. If GCC is used to compile the source file and `libnetpbm` is dynamically linked (i.e. not "baked into" the final binary), the following command may be used

    gcc transpose-frames.c -Wall -Werror -Wextra -L<directory where libnetpbm has been installed> -lnetpbm -o transpose-frames

which should work, at least on Linux. If the reader wishes to build the programs on Windows, they are more than welcome to do so. However, no guarantees about the validity of the command above on platforms other than Linux are provided.

Note that the reader may also need to modify the scripts used during video conversion if they wish to use a shell other than Bash.

# Usage Instructions
TODO

# File Format Specification
The file format used is based on encoding 8-bit wide columns of each frame using run-length encoding (RLE). For more information about why this approach was chosen and the details of the encoding and decoding process, see [the specification](./docs/format-spec.md).

# Resources
#### Video and Images
- The *Bad Apple* video used was downloaded from Internet Archive: [https://archive.org/details/bad-apple-resources](https://archive.org/details/bad-apple-resources).

#### Documentation and Further Reading
- A successful *Bad Apple* implementation for the TI-84 Plus CE using ZX7 (an implementation of LZ77/LZSS) for video compression: [https://github.com/Penguin-Spy/BADVIDEO](https://github.com/Penguin-Spy/BADVIDEO).
    - A port of ZX7: [https://github.com/antoniovillena/zx7b?tab=readme-ov-file](https://github.com/antoniovillena/zx7b?tab=readme-ov-file).
    - More information about ZX7: [https://ia902300.us.archive.org/view_archive.php?archive=/4/items/World_of_Spectrum_June_2017_Mirror/World%20of%20Spectrum%20June%202017%20Mirror.zip&file=World%20of%20Spectrum%20June%202017%20Mirror/sinclair/games-info/z/ZX7.txt](https://ia902300.us.archive.org/view_archive.php?archive=/4/items/World_of_Spectrum_June_2017_Mirror/World%20of%20Spectrum%20June%202017%20Mirror.zip&file=World%20of%20Spectrum%20June%202017%20Mirror/sinclair/games-info/z/ZX7.txt).
    - Some compression benchmarks including ZX7: [https://forums.atariage.com/topic/268244-data-compression-benchmark-dan-pletter-zx7-exomizer-pucrunch-megalz/](https://forums.atariage.com/topic/268244-data-compression-benchmark-dan-pletter-zx7-exomizer-pucrunch-megalz/).
- An interesting read about video compression, this served as inspiration for the compression algorithm used before the 8-bit block RLE approach was settled upon: [https://github.com/dunnousername/dunnousername.github.io/blob/master/bad_apple/bad_apple.md](https://github.com/dunnousername/dunnousername.github.io/blob/master/bad_apple/bad_apple.md).
- A discussion about compressing *Bad Apple* on Reddit (where an 8-bit block-based approach is mentioned): [https://www.reddit.com/r/Demoscene/comments/43lu9t/most_efficient_encoding_of_bad_apple/](https://www.reddit.com/r/Demoscene/comments/43lu9t/most_efficient_encoding_of_bad_apple/).
- The CE C/C++ Toolchain (and CE C libraries) documentation: [https://ce-programming.github.io/toolchain/index.html](https://ce-programming.github.io/toolchain/index.html).
- `libnetpbm` manual: [https://netpbm.sourceforge.net/doc/libnetpbm.html](https://netpbm.sourceforge.net/doc/libnetpbm.html).
- FFmpeg documentation: [https://www.ffmpeg.org/documentation.html](https://www.ffmpeg.org/documentation.html).
    - On piping the output of FFmpeg into another program (that uses `libnetpbm`): [https://www.drmaciver.com/2010/12/reading-video-frame-by-frame-with-ffmpeg/](https://www.drmaciver.com/2010/12/reading-video-frame-by-frame-with-ffmpeg/).

#### Calculator Hardware Specifications
- Cemetech hardware overview: [https://dev.cemetech.net/tools/ti84pce](https://dev.cemetech.net/tools/ti84pce).
- WikiTI: [https://wikiti.brandonw.net/index.php?title=WikiTI_Home](https://wikiti.brandonw.net/index.php?title=WikiTI_Home).
- A discussion thread on replacing the LCD on a TI-84 Plus CE: [https://www.ifixit.com/Answers/View/542293/Replacing+the+lcd+with+a+different+one.](https://www.ifixit.com/Answers/View/542293/Replacing+the+lcd+with+a+different+one.).
    - Some information about the LCD display (a GiantPlus GPM1421C0): [https://web.archive.org/web/20211230001857/https://www.giantplus.com.tw/en/prod_infos/35-inch-lcd-module-5](https://web.archive.org/web/20211230001857/https://www.giantplus.com.tw/en/prod_infos/35-inch-lcd-module-5).
- The LCD controller (an Arm PrimeCell PL111) technical reference manual: [https://developer.arm.com/documentation/ddi0293/c?lang=en](https://developer.arm.com/documentation/ddi0293/c?lang=en).