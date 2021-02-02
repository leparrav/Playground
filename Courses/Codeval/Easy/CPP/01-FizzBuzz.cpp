// https://www.codeeval.com/open_challenges/1/submit/
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char *argv[]) {
    ifstream in_file(argv[1]);
    string line;
    int X, Y, N;
    vector<string> tokens;
    while (in_file >> X >> Y >> N){
    	for (int i = 1; i <= N; i++){
    		string to_print = "";
    		if (i%X == 0) {
    			to_print += "F";
    		}
    		if (i%Y == 0){
    			to_print += "B";
    		}

    		if (to_print != ""){
    			cout << to_print;
    		}
    		else {
    			cout << i;
    		}
    		if (i != N) {
    			cout << " ";
    		}
    	}
    	cout << endl;
    }
    return 0;
}