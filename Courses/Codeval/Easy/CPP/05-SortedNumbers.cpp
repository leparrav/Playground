// https://www.codeeval.com/open_challenges/91/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

bool MyOrder(float x, float y){
	return (x<y);
}

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
    while (getline(in_file,line)){
    	vector<string> tokens;
    	vector<double> numbers;

    	Tokenize(line,tokens);

    	// Build a vector of float from our string line
    	for (vector<string>::iterator it = tokens.begin(); it != tokens.end(); it++){
    		float value = 0;
    		istringstream iss(*it);
    		iss >> value;
    		numbers.push_back(value);
    	}

    	// Sort it and print it
		sort(numbers.begin(), numbers.end(), MyOrder);
		for (int i = 0; i < numbers.size(); i++){
			printf("%4.3f", numbers[i]);
			if (i != numbers.size()-1)
				cout << " ";
			}

	 	cout << '\n';
	}

    return 0;
}

