import doors
import test_doors

if __name__ == "__main__":
    
    doors.run("small.txt")
    doors.run("large.txt")
    
    test_doors.test_condition()
    test_doors.test_condition2()
    
    test_doors.test_solver()
    test_doors.test_solver2()
    
    test_doors.test_key()
    test_doors.test_key2()
    test_doors.test_key3()
    test_doors.test_key4()
