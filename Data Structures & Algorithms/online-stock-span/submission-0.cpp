class StockSpanner {
    vector<int> arr;

public:
    StockSpanner() {}

    int next(int price) {
        arr.push_back(price);
        int i = arr.size() - 2;
        while (i >= 0 && arr[i] <= price) {
            i--;
        }
        return arr.size() - i - 1;
    }
};