#include <netpbm/pbm.h>

int main(int argc, char **argv) {
    pbm_init(&argc, argv);

    printf("Hello World! I should not compile without libnetpbm!\n");
    
    return 0;
}