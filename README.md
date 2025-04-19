# Monochrome Video Player for the TI-84 Plus CE

**By Lukas Broström and Muhammed Reza Mehdi <br>**
**DD1349, Group Project**

> **Rule 86:** If it exists, you can play *Bad Apple* on it <br> - *The Rules of the Internet*

For the reader who is not familiar with the TI-84 Plus CE, it is a graphing calculator manufactured by Texas Instruments as part of the TI-84 series of graphing calculators. The TI-84 Plus CE comes with some (for a calculator) surprisingly powerful hardware: it has a 24-bit Zilog eZ80 processor clocked at 48 MHz (true speed severely limited by wait states), 256 KB of RAM (154 KB user-accessible) and 4 MB of ROM (3 MB user accessible). For more information, see the [hardware overview on Cemetech](https://dev.cemetech.net/tools/ti84pce). As for the display, it is a 320x240 colour LCD with support for 16-bit colour, but the LCD controller (an Arm [PrimeCell PL111](https://developer.arm.com/documentation/ddi0293/c?lang=en)) supports more colour modes including a 1 bpp mode for reduced RAM usage (which is excellent for a monochrome video player). Since the TI-84 Plus CE has a display capable of showing at least two colours, the calculator should theoretically be capable of playing monochrome video, such as *Bad Apple* ([link to original on Nicovideo](https://www.nicovideo.jp/watch/sm8628149)), making playing *Bad Apple* on the calculator the end goal of this project (which hopefully is achievable in about three weeks, otherwise a terminal player will do).

# Goals
- Develop a video encoding utility capable of compressing (low FPS) monochrome video to a size that fits on the TI-84 Plus CE.
- Develop a monochrome video player capable of decoding and displaying video encoded in the developed format.
- Play *Bad Apple* on a TI-84 Plus CE or, if all else fails, the terminal.

# Dependencies
TODO

# Build Instructions
TODO