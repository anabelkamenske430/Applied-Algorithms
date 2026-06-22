import heapq
from astar import find_fastest_path

class CallDispatcher:
    def __init__(self, calls, priorities, ambulances, graph):
        """
        Initializes the dispatcher with call data, priority mapping, ambulance locations, and the city graph.
        """
        self.call_queue = []
        self.priorities = priorities              # dict: Call Type → Priority
        self.ambulances = ambulances              # dict: Ambulance ID → Location
        self.graph = graph                        # Graph object
        self._load_calls(calls)

    def _load_calls(self, calls):
        """
        Loads calls into a priority queue based on urgency.
        """
        for call in calls:
            priority = self.priorities.get(call['Call Type'], 3)
            call_id = call['Call ID']
            heapq.heappush(self.call_queue, (priority, call_id, call))  # Tie-breaker: call_id

    def has_calls(self):
        """
        Returns True if there are calls left to dispatch.
        """
        return len(self.call_queue) > 0

    def get_next_call(self):
        """
        Retrieves the next highest-priority call from the queue.
        """
        if self.call_queue:
            return heapq.heappop(self.call_queue)[2]  # Return the call dict
        return None

    def dispatch_next_call(self):
        """
        Assigns the best ambulance to the next call and prints dispatch details.
        """
        if not self.has_calls() or not self.ambulances:
            print("🚫 No calls or ambulances available.")
            return

        call = self.get_next_call()
        call_location = call['Location']
        call_type = call['Call Type']
        call_id = call['Call ID']

        best_ambulance = None
        best_cost = float('inf')
        best_path = []

        # Find the closest ambulance
        for amb_id, amb_location in self.ambulances.items():
            cost, path = find_fastest_path(self.graph, amb_location, call_location)
            if cost < best_cost:
                best_cost = cost
                best_path = path
                best_ambulance = amb_id

        # Dispatch the selected ambulance
        if best_ambulance:
            print(f"\n🚑 Dispatching {best_ambulance} to Call {call_id} ({call_type}) at {call_location}")
            print("🛣️ Route:", " → ".join(best_path))
            print(f"🕒 Estimated Travel Cost: {best_cost}")

            # Update ambulance location
            self.ambulances[best_ambulance] = call_location
        else:
            print(f"⚠️ No ambulance could reach Call {call_id} at {call_location}")