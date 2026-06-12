public class MinStack {
    private Stack<int> mainStack;
    private Stack<int> minTrackerStack;

    public MinStack() {
        mainStack = new Stack<int>();
        minTrackerStack = new Stack<int>();
    }
    
    public void Push(int val) {
        mainStack.Push(val);

        if (minTrackerStack.Count == 0) {
            minTrackerStack.Push(val);
        } else {
            int currentMin = Math.Min(val, minTrackerStack.Peek());
            minTrackerStack.Push(currentMin);
        }
    }
    
    public void Pop() {
        mainStack.Pop();
        minTrackerStack.Pop();
    }
    
    public int Top() {
        return mainStack.Peek();
    }
    
    public int GetMin() {
        return minTrackerStack.Peek();
    }
}