class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank = 0   # overall gas balance
        curr_tank = 0    # gas balance from current start
        start = 0        # possible starting index

        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]

            # if tank goes negative, can't start from 'start'
            if curr_tank < 0:
                start = i + 1   # next station is new candidate
                curr_tank = 0   # reset tank

        # if total gas < total cost → impossible
        if total_tank < 0:
            return -1
        return start
