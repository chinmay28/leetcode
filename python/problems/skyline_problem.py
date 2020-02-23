import heapq


class Solution:
    def getSkyline(self, buildings):
        coords = self.makecoords(buildings)
        print(coords)
        heap = []
        heapq.heappush(heap, 0)
        maxval = 0
        output = []
        for x, y, status in coords:
            print(x, y, status)
            if (status == 's'):
                heapq.heappush(heap, -y)
                if (maxval != -heap[0]):
                    output.append([x, y])
                    maxval = -heap[0]
            elif (status == 'e'):
                heap.remove(-y)
                if (maxval != -heap[0]):
                    output.append([x, -heap[0]])
                    maxval = -heap[0]
            print(heap)
        return (output)

    def makecoords(self, buildings):
        coords = []
        for Li, Ri, Hi in buildings:
            coords.append([Li, Hi, "s"])
            coords.append([Ri, Hi, "e"])
        coords = sorted(coords, key=lambda x: x[0])
        return coords


Solution().getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]])
