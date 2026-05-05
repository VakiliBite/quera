us_input_count = int(input())

def main():
    member_list = input().split()[:us_input_count]
    
    present = []
    
    for new in member_list:
        for old in reversed(present):
                
            print(f"{new}: salam {old}!")
        present.append(new)
            
    for leaver in member_list:
        print(f"{leaver}: khodafez bacheha!")
        
        for newleaver in present:
            if newleaver != leaver:
                print(f"{newleaver}: khodafez {leaver}!")
        present.remove(leaver)
                
            
main()