// https://www.codeeval.com/open_challenges/8/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

// Split string functions
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
    ifstream in_file(argv[1]);
    string line;
    vector<string> tokens;
    while (getline(in_file, line)) {
    	if (line != ""){
	    	Tokenize(line,tokens);
	    	string reversed = "";
	    	while(!tokens.empty()){
	    		reversed += tokens.back();
	    		tokens.pop_back();
	    		if (tokens.size() != 0){
	    			reversed += " ";
	    		}
	    	}
	    	cout << reversed << endl;
    	}
    }
}