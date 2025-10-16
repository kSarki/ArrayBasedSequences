def split_evens_odds(arr):
    if not arr:
        print("Array is empty!")
        return [], []
    
    evens = []
    odds = []
    
    print(f"\nOriginal Array: {arr}")
    print("\nProcessing:")
    print(f"{'Index':<8} {'Value':<8} {'Type':<10} {'Evens':<25} {'Odds':<25}")
    print("-" * 76)
    
    for i, num in enumerate(arr):
        if num % 2 == 0:
            evens.append(num)
            num_type = "Even"
        else:
            odds.append(num)
            num_type = "Odd"
        
        print(f"{i:<8} {num:<8} {num_type:<10} {str(evens):<25} {str(odds):<25}")
    
    print("-" * 76)
    print(f"\nEven Numbers: {evens}")
    print(f"Odd Numbers: {odds}")
    
    return evens, odds


def split_evens_odds_in_place(arr):
    if not arr:
        print("Array is empty!")
        return arr
    
    print(f"\nOriginal Array: {arr}")
    print("\nIn-place separation (evens on left, odds on right):")
    
    left = 0
    right = len(arr) - 1
    
    print(f"{'Step':<6} {'Left':<6} {'Right':<7} {'Array':<40}")
    print("-" * 59)
    
    step = 1
    print(f"{step:<6} {left:<6} {right:<7} {str(arr):<40}")
    
    while left < right:
        while left < right and arr[left] % 2 == 0:
            left += 1
        
        while left < right and arr[right] % 2 != 0:
            right -= 1
        
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            step += 1
            print(f"{step:<6} {left:<6} {right:<7} {str(arr):<40}")
            left += 1
            right -= 1
    
    print("-" * 59)
    print(f"\nFinal Array (Evens first, then Odds): {arr}")
    
    return arr


def partition_array(arr):
    if not arr:
        print("Array is empty!")
        return arr, 0
    
    print(f"\nOriginal Array: {arr}")
    print("\nPartitioning array (evens on left, odds on right):")
    
    partition_index = 0
    
    print(f"{'Step':<6} {'Index':<7} {'Value':<8} {'Partition':<12} {'Array':<40}")
    print("-" * 73)
    
    step = 1
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i], arr[partition_index] = arr[partition_index], arr[i]
            print(f"{step:<6} {i:<7} {arr[partition_index]:<8} {partition_index:<12} {str(arr):<40}")
            partition_index += 1
            step += 1
    
    print("-" * 73)
    print(f"\nPartitioned Array: {arr}")
    print(f"Partition Index: {partition_index} (evens: 0 to {partition_index-1}, odds: {partition_index} to {len(arr)-1})")
    
    return arr, partition_index


def run_split_evens_odds():
    print("\n" + "="*60)
    print("PROJECT 3: SPLIT EVENS-ODDS")
    print("="*60)
    
    while True:
        print("\n1. Split into Separate Arrays (Evens and Odds)")
        print("2. In-Place Split (Two-Pointer Approach)")
        print("3. Partition Array (Single-Pass)")
        print("4. Back to Main Menu")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice in ['1', '2', '3']:
            try:
                input_str = input("\nEnter numbers separated by spaces (e.g., 1 2 3 4 5): ").strip()
                if not input_str:
                    print("Invalid input!")
                    continue
                
                arr = list(map(int, input_str.split()))
                
                if choice == '1':
                    evens, odds = split_evens_odds(arr)
                
                elif choice == '2':
                    result = split_evens_odds_in_place(arr.copy())
                
                elif choice == '3':
                    result, partition_idx = partition_array(arr.copy())
            
            except ValueError:
                print("Invalid input! Please enter numbers only.")
        
        elif choice == '4':
            break
        
        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    run_split_evens_odds()
