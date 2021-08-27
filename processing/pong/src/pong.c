#include <stdio.h>
#include <time.h>
#include <string.h>

#define BUF_LEN 256

int main(void) {
    char buf[BUF_LEN] = {0};
    time_t rawtime = time(NULL);
    struct tm *ptm = gmtime(&rawtime);
    strftime(buf, BUF_LEN, "%FT%X.000Z", ptm);

    printf("{\"msg\": \"pong\", \"process\": \"c\", \"created\":\"%s\"}", buf);

    return 0;
}
