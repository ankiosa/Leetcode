class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int nrows = matrix.size();
        int ncols = matrix[0].size();
        int srow = 0; int scol = ncols-1;
        if(target<matrix[0][0] || target>matrix[nrows-1][scol]) return false;
        while((srow<=nrows-1 && scol>=0)){

            if(matrix[srow][scol]==target) return true;
            else if(matrix[srow][scol]<target) srow+=1;
            else scol-=1;
        }
        cout <<"ok" << endl;
        return matrix[nrows-1][0]==target;
    }
};