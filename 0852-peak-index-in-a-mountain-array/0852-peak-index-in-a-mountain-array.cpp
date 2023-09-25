class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        
        
        int len_arr = arr.size();
        int s=0; int e= len_arr-1;
        int mid = s+(e-s)/2;
        while(s<=e){
            cout << s << " " << mid << " " << e << endl;
            if(arr[mid-1]<arr[mid] && arr[mid+1]<arr[mid]) return mid;
            else if((arr[mid-1]<arr[mid] && arr[mid+1]>arr[mid])) s=mid;
            else if((arr[mid-1]>arr[mid] && arr[mid+1]<arr[mid])) e=mid;
            mid = s+(e-s)/2;
            
        } 
        return 0;
    }
};