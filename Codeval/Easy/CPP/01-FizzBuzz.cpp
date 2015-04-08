// https://www.codeeval.com/open_challenges/1/submit/
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// Split string functions - I miss Python
void Tokenize(const string& str,
                      vector<string>& tokens,
                      const string& delimiters = " "){

    // Skip delimiters at beginning.
    string::size_type lastPos = str.find_first_not_of(delimiters, 0);
    // Find first "non-delimiter".
    string::size_type pos     = str.find_first_of(delimiters, lastPos);

    while (string::npos != pos || string::npos != lastPos)
    {
        // Found a token, add it to the vector.
        tokens.push_back(str.substr(lastPos, pos - lastPos));
        // Skip delimiters.  Note the "not_of"
        lastPos = str.find_first_not_of(delimiters, pos);
        // Find next "non-delimiter"
        pos = str.find_first_of(delimiters, lastPos);
    }
}



int main(int argc, char *argv[]) {
    ifstream stream(argv[1]);
    string line;
    vector<string> tokens;
    while (getline(stream, line)) {
        Tokenize(line, tokens);
    }
    return 0;
}