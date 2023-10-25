import time
import os
import speedtest

def get_wifi_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    return download_speed

def display_graph(speed):
    graph_length = int(speed)
    graph = '|' + '#' * graph_length + ' ' * (50 - graph_length) + '|'
    print(f'Download Speed: {speed:.2f} Mbps')
    print(graph)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        speed = get_wifi_speed()
        clear_console()
        display_graph(speed)
        time.sleep(1)

if __name__ == "__main__":
    main()
