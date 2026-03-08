#include "topic.hpp"
      #include <cassert>

      int main() {
        CliArgs args{};
args.input = "../fixtures/tasks.txt";
        assert(run(args) == "hello thread-pool\n");
        return 0;
      }
