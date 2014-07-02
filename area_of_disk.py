# computing an area of a disk

def area_of_disk(radius):
    area = 3.14 * (radius ** 2)
    print "area of disk %d: %d" %(radius,area)
    return area
    
def area_of_ring(outer, inner):
    ring_area = (outer - inner)
    print "area of ring:", ring_area
    return ring_area
        
outer = area_of_disk(5)
inner = area_of_disk(3)

area_of_ring(outer, inner)
