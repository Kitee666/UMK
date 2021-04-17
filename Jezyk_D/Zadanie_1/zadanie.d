extern (C) int fibonacci(int n);

import std.stdio : writeln;
import std.conv;
import std.file : write;

int main(char[][] args)
{
    if (args.length != 3)
    {
        writeln("Usage: ", args[0], " number output_file");
        return 1;
    }
    write(args[2], to!string(fibonacci(to!int(args[1]))));
    return 0;
}
