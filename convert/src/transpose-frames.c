#include <netpbm/pbm.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdio.h>

void transpose_frame(uint8_t* frame, size_t rows, size_t columns, uint8_t* frame_transpose) {
    for (size_t i = 0; i < columns; i++) {
        for (size_t j = 0; j < rows; j++) {
            *(frame_transpose + j + i * rows) = *(frame + i + j * columns);
        }
    }
}

int main(int argc, char **argv) {
    int c;
    int columns, rows, format;

    pbm_init(&argc, argv);

    // All frames are assumed to have identical headers.

    // Read a PBM header.
    pbm_readpbminit(stdin, &columns, &rows, &format);

    // TODO: Write (part of) RLEMV header to stdout?
    
    // Buffers reused to reduce memory allocations.
    size_t frame_columns = columns / 8;
    size_t frame_size = rows * frame_columns;
    uint8_t* frame = malloc(frame_size);
    uint8_t* frame_transpose = malloc(frame_size);

    // Read the first frame from stdin.
    fread(frame, 1, frame_size, stdin);

    // Transpose the first frame and write to stdout.
    transpose_frame(frame, rows, frame_columns, frame_transpose);
    fwrite(frame_transpose, frame_size, 1, stdout);

    // Slightly "hacky" way to read a sequence of PBMs from stdin until reaching EOF.
    while ((c = getc(stdin)) != EOF) {
        ungetc(c, stdin);

        pbm_readpbminit(stdin, &columns, &rows, &format);
        fread(frame, 1, frame_size, stdin);

        transpose_frame(frame, rows, frame_columns, frame_transpose);
        fwrite(frame_transpose, frame_size, 1, stdout);
    }

    // Free allocated buffers.
    free(frame);
    free(frame_transpose);
    
    return 0;
}