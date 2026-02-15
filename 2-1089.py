import sys

def solve():
    while True:
        try:
            line1 = sys.stdin.readline()
            if not line1: 
                break
                
            n = int(line1.strip())
            
            if n == 0:
                break
                
            line2 = sys.stdin.readline()
            if not line2:
                break
                
            h = list(map(int, line2.split()))
            
            while len(h) < n:
                h.extend(map(int, sys.stdin.readline().split()))

            n_peaks = 0
            
            # Verificação circular usando índices
            for i in range(n):
                # Trata h[i-1] como o último elemento se i=0
                # O (i+1)%n volta para o primeiro se i=n-1
                prev_val = h[i - 1]
                curr_val = h[i]
                next_val = h[(i + 1) % n]
                
                # Lógica: Pico ou Vale
                if (curr_val > prev_val and curr_val > next_val) or \
                   (curr_val < prev_val and curr_val < next_val):
                    n_peaks += 1
            
            print(n_peaks)
            
        except EOFError:
            break
        except ValueError:
            continue

if __name__ == "__main__":
    solve()