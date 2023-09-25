class Solution {
public:
    bool isValid(string s) {

        map<char, char> mymap;

        mymap[']'] = '[';
        mymap['}'] = '{';
        mymap[')'] = '(';

        vector<char> stringchar;

        for(auto x:s){
            if(x=='{' or x=='[' or x=='('){
                stringchar.push_back(x);
            }
            else{
                if(stringchar.empty() or mymap[x]!=stringchar.back()){
                    return false;
                }
                else{
                    stringchar.pop_back();
                }
            }
        }
        for(auto x:stringchar){
            cout << x << "\n";
        }
 
        return stringchar.empty();
        
    }
};