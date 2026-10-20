
# Emergency Ambulance Route Finder

import heapq

graph = {
    "Ambulance": {
        "Main Road": 4,
        "Market": 7
    },
    "Main Road": {
        "Ambulance": 4,
        "Bridge": 3,
        "Hospital A": 8
    },
    "Market": {
        "Ambulance": 7,
        "Bridge": 2,
        "Hospital B": 6
    },
    "Bridge": {
        "Main Road": 3,
        "Market": 2,
        "Hospital A": 4,
        "Hospital B": 5
    },
    "Hospital A": {
        "Main Road": 8,
        "Bridge": 4
    },
    "Hospital B": {
        "Market": 6,
        "Bridge": 5
    }
}

def dijkstra(graph, start, destination):
    distances = {place: float("inf") for place in graph}
    previous = {place: None for place in graph}

    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        time, current = heapq.heappop(priority_queue)

        if time > distances[current]:
            continue

        if current == destination:
            break

        for neighbor, road_time in graph[current].items():
            new_time = time + road_time

            if new_time < distances[neighbor]:
                distances[neighbor] = new_time
                previous[neighbor] = current
                heapq.heappush(
                    priority_queue, (new_time, neighbor)
                )

    if distances[destination] == float("inf"):
        return None, float("inf")

    route = []
    current = destination

    while current is not None:
        route.append(current)
        current = previous[current]

    route.reverse()
    return route, distances[destination]


print("=== EMERGENCY AMBULANCE ROUTE FINDER ===")

print("\nAvailable Locations:")
for place in graph:
    print("-", place)

start = input("\nEnter ambulance location: ").strip()
hospital = input("Enter destination hospital: ").strip()

if start not in graph or hospital not in graph:
    print("Invalid location! Please enter a listed location.")
else:
    route, total_time = dijkstra(graph, start, hospital)

    if route is None:
        print("No route available.")
    else:
        print("\nBest Route:")
        print(" -> ".join(route))
        print("Estimated Travel Time:", total_time, "minutes")
