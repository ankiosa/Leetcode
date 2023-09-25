class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int nrows = matrix.size();
        int ncols = matrix[0].size();
        int e = nrows*ncols-1;
        int s =0;
        if(s==e) return matrix[s][e]==target;
        while(s<=e){
        int mid = (s+e)/2;
        int row_index = (mid)/ncols;
        int col_index = (mid)%ncols;
        cout << mid << " " << s <<" " << e << " " << row_index <<" " << col_index << endl;
        if(matrix[row_index][col_index]<target) s=(row_index*ncols+col_index+1);
        else if(matrix[row_index][col_index]>target) e=(row_index*ncols+col_index-1);
        else return true;
        }
        return false;
            
        
        
    }
};