int func(int x) {
    int y = 2 * x;

    return y;
}

int func2(int x, int y) {
    int z = x + y;
    return z;
}

int main() {
    int x = 3;
    int z = x + 2 * func2(x + 2*func(1), 3 + 4) - 1;
}
