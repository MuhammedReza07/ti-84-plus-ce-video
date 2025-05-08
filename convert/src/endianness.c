#include <stdint.h>

uint32_t swap_endianness_u32(uint32_t value) {
    return ((value & 0xff000000) >> 24)
    | ((value & 0xff0000) >> 8)
    | ((value & 0xff00) << 8)
    | ((value & 0xff) << 24);
}

uint32_t host_to_le_u32(uint32_t value) {
    uint16_t a = 1;

    // If a is little-endian.
    if ((uint8_t*)(&a) == 1) {
        return value;
    } else {
        return swap_endianness_u32(value);
    }
}

uint32_t host_to_be_u32(uint32_t value) {
    uint16_t a = 1;

    // If a is little-endian.
    if ((uint8_t*)(&a) == 1) {
        return swap_endianness_u32(value);
    } else {
        return value;
    }
}