#!/usr/bin/env python3 
import unittest
import cspbAlg 

class CSPBTest(unittest.TestCase):

    def test_case_1(self):
        # testing output when student needs just one more required course and nothing else 
        input = [1300, 2824, 2270, 3104, 3308, 2400, 3702, 3403, 4502, 2820, 3022, 4122] 
        inputHours = 20
        inputElectives = [] 
        dontWant = []
        inputSemester = 0
        p = cspbAlg.basicAlg(input, inputHours, inputElectives, inputSemester, dontWant)
        self.assertEqual(p, ([3155], 45), "test_case_1 error")

    def test_case_2(self):
        # for low-hour commitment student in first semester, just return 1300 
        input = [] 
        inputHours = 10
        inputElectives = [3022] 
        dontWant = []
        inputSemester = 0
        p = cspbAlg.basicAlg(input, inputHours, inputElectives, inputSemester, dontWant)
        self.assertEqual(p, ([1300], 4), "test_case_2 error")

    def test_case_3(self):
        #for mid-range commitment student in first semester, not wanting cog sci or info vis 
        # prioritizing 3022 over 2824 
        input = [] 
        inputHours = 25
        inputElectives = [3022] 
        dontWant = [3702, 4122]
        inputSemester = 0
        p = cspbAlg.basicAlg(input, inputHours, inputElectives, inputSemester, dontWant)
        self.assertEqual(p, ([1300, 3022], 7), "test_case_3 error")

    def test_case_4(self):
        #for mid-range commitment student in first semester, not wanting cog sci or info vis 
        # should default to 2824 over other electives 
        input = [] 
        inputHours = 25
        inputElectives = [] 
        dontWant = [3702, 4122]
        inputSemester = 0
        p = cspbAlg.basicAlg(input, inputHours, inputElectives, inputSemester, dontWant)
        self.assertEqual(p, ([1300, 2824], 7), "test_case_4 error")
    
    def test_case_5(self):
        # with a full schedule for first semester, maximize courses taken without unwated electives
        input = [] 
        inputHours = 40
        inputElectives = [] 
        dontWant = [3702, 4122]
        inputSemester = 0
        p = cspbAlg.basicAlg(input, inputHours, inputElectives, inputSemester, dontWant)
        self.assertEqual(p, ([1300, 2824, 3022], 10), "test_case_5 error")
    
    def test_case_6(self):
        # part-time first-sem schedule, no time for discrete, but time for cog sci - time for 4122, but not eligible
        input = [] 
        inputHours = 20
        inputElectives = [] 
        dontWant = []
        inputSemester = 0
        p = cspbAlg.basicAlg(input, inputHours, inputElectives, inputSemester, dontWant)
        self.assertEqual(p, ([1300, 3702], 7), "test_case_6 error")

    def test_case_7(self):
        # 2 classes left - 2400 & 3403 - haven't fulfilled prereq yet 
        input = [1300, 2824, 2270, 3308, 3104, 3155, 3702, 4502, 3022, 2820, 3202] 
        inputHours = 25
        inputElectives = [3403] 
        dontWant = []
        inputSemester = 1
        p = cspbAlg.basicAlg(input, inputHours, inputElectives, inputSemester, dontWant)
        self.assertEqual(p, ([2400], 41), "test_case_7 error")

    def test_case_8(self):
        # make sure prereqs are taken for wanted electives 
        input = [1300, 2824, 2270, 3308, 3104, 2400, 3702] 
        inputHours = 25
        inputElectives = [3302, 4622] 
        dontWant = []
        inputSemester = 0
        p = cspbAlg.basicAlg(input, inputHours, inputElectives, inputSemester, dontWant)
        self.assertEqual(p, ([3022, 2820], 31), "test_case_8 error")

    def test_case_9(self):
        # make sure prereqs are taken for wanted electives - continuation of 8
        input = [1300, 2824, 2270, 3308, 3104, 2400, 3702] 
        inputHours = 25
        inputElectives = [3302, 4622] 
        dontWant = []
        inputSemester = 1
        p = cspbAlg.basicAlg(input, inputHours, inputElectives, inputSemester, dontWant)
        self.assertEqual(p, ([3022, 3403], 32), "test_case_9 error")

    def test_case_10(self):
        # make sure prereqs are taken for wanted electives - continuation of 8 and 9 
        input = [1300, 2824, 2270, 3308, 3104, 2400, 3702, 3022, 3403] 
        inputHours = 25
        inputElectives = [3302, 4622] 
        dontWant = []
        inputSemester = 2
        p = cspbAlg.basicAlg(input, inputHours, inputElectives, inputSemester, dontWant)
        self.assertEqual(p, ([2820, 3155], 39), "test_case_10 error")

    def test_case_11(self):
        # make sure 2820 is taken, without specifying it's wanted 
        input = [1300, 2824, 2270, 3308, 3104, 2400, 3702] 
        inputHours = 25
        inputElectives = [3302] 
        dontWant = []
        inputSemester = 0
        p = cspbAlg.basicAlg(input, inputHours, inputElectives, inputSemester, dontWant)
        self.assertEqual(p, ([2820, 3155], 32), "test_case_11 error")

    def test_case_12(self):
        # testing feedback for one last semester where chosen elective is offered 
        input = [1300, 3702, 2824, 2270, 3104, 2400, 3308, 2820, 3022, 3403, 3155, 4502]
        inputHours = 15
        inputElectives = [3302] 
        dontWant = [3753, 4122, 4622, 3202]
        inputSemester = 3
        p = cspbAlg.basicAlg(input, inputHours, inputElectives, inputSemester, dontWant)
        self.assertEqual(p, ([3302], 45), "test_case_12 error")

    def test_case_13(self):
        # testing feedback for one last semester where chosen elective is not offered 
        input = [1300, 3702, 2824, 2270, 3104, 2400, 3308, 2820, 3022, 3403, 3155, 4502]
        inputHours = 15
        inputElectives = [3302] 
        dontWant = [3753, 4122, 4622, 3202]
        inputSemester = 4
        p = cspbAlg.basicAlg(input, inputHours, inputElectives, inputSemester, dontWant)
        self.assertEqual(p, ([], 42), "test_case_13 error")
    
    def test_case_14(self):
        # testing feedback for one last semester where course offered, but not enough hours 
        input = [1300, 3702, 2824, 2270, 3104, 2400, 3308, 2820, 3022, 3403, 3155, 4502]
        inputHours = 10
        inputElectives = [3302] 
        dontWant = [3753, 4122, 4622, 3202]
        inputSemester = 3
        p = cspbAlg.basicAlg(input, inputHours, inputElectives, inputSemester, dontWant)
        self.assertEqual(p, ([], 42), "test_case_14 error")

    def test_case_15(self):
        # testing feedback for second semester, without data structures 
        input = [1300]
        inputHours = 40
        inputElectives = [2820, 3022, 3403, 3302] 
        dontWant = [3753, 4122, 4622, 3202]
        inputSemester = 1
        p = cspbAlg.basicAlg(input, inputHours, inputElectives, inputSemester, dontWant)
        self.assertEqual(p, ([3022, 2824, 3702], 13), "test_case_15 error")
    
    def test_case_16(self):
        # testing feedback for third semester, continuation of previous 
        input = [1300, 3022, 2824, 3702]
        inputHours = 40
        inputElectives = [2820, 3022, 3403, 3302] 
        dontWant = [3753, 4122, 4622, 3202]
        inputSemester = 2
        p = cspbAlg.basicAlg(input, inputHours, inputElectives, inputSemester, dontWant)
        self.assertEqual(p, ([2820, 2270, 3308], 23), "test_case_16 error")

    def test_case_17(self):
        # testing feedback for fourth semester, continuation of previous 
        input = [1300, 3022, 2824, 3702, 2820, 2270, 3308]
        inputHours = 40
        inputElectives = [2820, 3022, 3403, 3302] 
        dontWant = [3753, 4122, 4622, 3202]
        inputSemester = 3
        p = cspbAlg.basicAlg(input, inputHours, inputElectives, inputSemester, dontWant)
        self.assertEqual(p, ([3302, 3104, 4502], 33), "test_case_17 error")

    def test_case_18(self):
        # testing feedback for fifth semester, continuation of previous 
        input = [1300, 3022, 2824, 3702, 2820, 2270, 3308, 3302, 3104, 4502]
        inputHours = 40
        inputElectives = [2820, 3022, 3403, 3302] 
        dontWant = [3753, 4122, 4622, 3202]
        inputSemester = 4
        p = cspbAlg.basicAlg(input, inputHours, inputElectives, inputSemester, dontWant)
        self.assertEqual(p, ([2400, 3155], 41), "test_case_18 error")

    def test_case_19(self):
        # testing feedback for sixth semester, continuation of previous 
        # OK because cyber being offered in last semester 
        input = [1300, 3022, 2824, 3702, 2820, 2270, 3308, 3302, 3104, 4502, 2400, 3155]
        inputHours = 40
        inputElectives = [2820, 3022, 3403, 3302] 
        dontWant = [3753, 4122, 4622, 3202]
        inputSemester = 5
        p = cspbAlg.basicAlg(input, inputHours, inputElectives, inputSemester, dontWant)
        self.assertEqual(p, ([3403], 45), "test_case_19 error")
    
    def test_case_20(self):
        # testing feedback for second semester STARTING WITH SUMMER 22, without data structures
        # same output  as previous 
        input = [1300]
        inputHours = 40
        inputElectives = [2820, 3022, 3403, 3302] 
        dontWant = [3753, 4122, 4622, 3202]
        inputSemester = 0
        p = cspbAlg.basicAlg(input, inputHours, inputElectives, inputSemester, dontWant)
        self.assertEqual(p, ([3022, 2824, 3702], 13), "test_case_20 error")

    def test_case_21(self):
        # testing feedback for third semester STARTING WITH SUMMER 22
        # DIFFERENT - no 2820, so 2400 in place of 2820 and 3308
        input = [1300, 3022, 2824, 3702]
        inputHours = 40
        inputElectives = [2820, 3022, 3403, 3302] 
        dontWant = [3753, 4122, 4622, 3202]
        inputSemester = 1
        p = cspbAlg.basicAlg(input, inputHours, inputElectives, inputSemester, dontWant)
        self.assertEqual(p, ([2270, 2400], 21), "test_case_21 error")
    
    def test_case_22(self):
        # testing feedback for third semester STARTING WITH SUMMER 22
        # DIFFERENT 
        input = [1300, 3022, 2824, 3702, 2270, 2400]
        inputHours = 40
        inputElectives = [2820, 3022, 3403, 3302] 
        dontWant = [3753, 4122, 4622, 3202]
        inputSemester = 2
        p = cspbAlg.basicAlg(input, inputHours, inputElectives, inputSemester, dontWant)
        self.assertEqual(p, ([2820, 3104, 3308], 31), "test_case_22 error")
    
    def test_case_23(self):
        # testing feedback for third semester STARTING WITH SUMMER 22
        # DIFFERENT - FINISHED SEMESTER EARLY 
        input = [1300, 3022, 2824, 3702, 2270, 2400, 2820, 3104, 3308]
        inputHours = 40
        inputElectives = [2820, 3022, 3403, 3302] 
        dontWant = [3753, 4122, 4622, 3202]
        inputSemester = 3
        p = cspbAlg.basicAlg(input, inputHours, inputElectives, inputSemester, dontWant)
        self.assertEqual(p, ([3403, 3302, 3155, 4502], 45), "test_case_23 error")

    def test_case_24(self): 
        # Version one, cases 15-19 
        input = [1300]
        inputHours = 40
        inputElectives = [2820, 3022, 3403, 3302] 
        dontWant = [3753, 4122, 4622, 3202]
        inputSemester = [1, 2, 3, 4, 5]
        p = cspbAlg.multipleSemesters(input, inputHours, inputElectives, inputSemester, dontWant)
        self.assertEqual(p, ({1: [3022, 2824, 3702], 2: [2820, 2270, 3308], 3: [3302, 3104, 4502], 4: [2400, 3155], 5: [3403]}), "test_case_24 error")
    
    def test_case_25(self): 
        # Version two, cases 20-23 
        input = [1300]
        inputHours = 40
        inputElectives = [2820, 3022, 3403, 3302] 
        dontWant = [3753, 4122, 4622, 3202]
        inputSemester = [0, 1, 2, 3, 4, 5]
        p = cspbAlg.multipleSemesters(input, inputHours, inputElectives, inputSemester, dontWant)
        self.assertEqual(p, ({0: [3022, 2824, 3702], 1: [2270, 2400], 2: [2820, 3104, 3308], 3: [3403, 3302, 3155, 4502]}), "test_case_25 error")
  
    def test_case_26(self): 
        # personal version for multiple - 30h
        input = [1300, 2270, 2824, 3702, 2400, 3308, 3104]
        inputHours = 30
        inputElectives = [2820, 3022, 3403, 3302] 
        dontWant = [3753, 4122, 4622, 3202]
        inputSemester = [0, 1, 2]
        p = cspbAlg.multipleSemesters(input, inputHours, inputElectives, inputSemester, dontWant)
        self.assertEqual(p, ({0: [3022, 2820, 4502], 1: [3403, 3302], 2: [3155]}), "test_case_26 error")
  
    def test_case_27(self): 
        # personal version for multiple - 25h
        input = [1300, 2270, 2824, 3702, 2400, 3308, 3104]
        inputHours = 25
        inputElectives = [2820, 3022, 3403, 3302] 
        dontWant = [3753, 4122, 4622, 3202]
        inputSemester = [0, 1, 2]
        p = cspbAlg.multipleSemesters(input, inputHours, inputElectives, inputSemester, dontWant)
        self.assertEqual(p, ({0: [3022, 2820], 1: [3403, 3302, 4502], 2: [3155]}), "test_case_27 error")
    
    def test_case_28(self):
        # valid input
        input = [1300, 3022, 2824, 3702, 2270, 2400, 2820, 3104, 3308]
        inputElectives = [2820, 3022, 3403, 3302] 
        p = cspbAlg.validInputElectives(inputElectives, input)
        self.assertEqual(p, (1), "test_case_28 error")

    def test_case_29(self):
        # invalid input
        input = [1300, 3022, 2824, 3702, 2270, 2400, 2820, 3104, 3308, 4502, 3287]
        inputElectives = [2820, 3022, 3403, 3302] 
        p = cspbAlg.validInputElectives(inputElectives, input)
        self.assertEqual(p, (0), "test_case_29 error")

    def test_case_30(self):
        # invalid input
        input = [1300, 3022, 2824, 2270, 2400, 3104, 3308]
        inputElectives = [2820, 3022, 3403, 3302, 3702, 4502, 2820] 
        p = cspbAlg.validInputElectives(inputElectives, input)
        self.assertEqual(p, (0), "test_case_30 error")

    def test_case_31(self):
        # valid input
        input = []
        inputElectives = [] 
        p = cspbAlg.validInputElectives(inputElectives, input)
        self.assertEqual(p, (1), "test_case_31 error")

    def test_case_32(self):
        # valid input
        input = []
        dontWant = [] 
        p = cspbAlg.validDontWant(dontWant)
        self.assertEqual(p, (1), "test_case_32 error")

    def test_case_33(self):
        # valid input
        input = []
        dontWant = [3403, 3753, 4622, 3202] 
        p = cspbAlg.validDontWant(dontWant)
        self.assertEqual(p, (1), "test_case_33 error")

    def test_case_34(self):
        # invalid input - too many credits 
        input = []
        dontWant = [3403, 3753, 4622, 3202, 3702, 3022, 2820] 
        p = cspbAlg.validDontWant(dontWant)
        self.assertEqual(p, (0), "test_case_34 error")
    
    def test_case_35(self):
        # valid input
        input = []
        dontWant = [3403] 
        p = cspbAlg.validDontWant(dontWant)
        self.assertEqual(p, (1), "test_case_35 error")

    def test_case_36(self):
        # valid input for 1300
        input = []
        take = [] 
        course = 1300
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (True), "test_case_36 error")

    def test_case_37(self):
        # invalid input for 1300
        input = [1300]
        take = [] 
        course = 1300
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (False), "test_case_37 error")
    
    def test_case_38(self):
        # valid input for 2824 
        input = []
        take = [1300] 
        course = 2824
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (True), "test_case_38 error")

    def test_case_39(self):
        # invalid input for 2824 
        input = []
        take = [] 
        course = 2824
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (False), "test_case_39 error")

    def test_case_40(self):
        # valid input for 3702 
        input = []
        take = [1300] 
        course = 3702
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (True), "test_case_40 error")

    def test_case_41(self):
        # invalid input for 3702 
        input = []
        take = [] 
        course = 3702
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (False), "test_case_41 error")

    def test_case_42(self):
        # valid input for 3702 
        input = [1300, 2824, 2270, 2820, 4622, 2400, 3104]
        take = [4502] 
        course = 3702
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (True), "test_case_40 error")

    def test_case_43(self):
        # valid input for 2400 
        input = [1300, 2824, 3702, 2270]
        take = [] 
        course = 2400
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (True), "test_case_43 error")

    def test_case_44(self):
        # invalid input for 2400 
        input = []
        take = [] 
        course = 2400
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (False), "test_case_44 error")

    def test_case_45(self):
        # invalid input for 2400 
        input = [1300, 2824, 2270, 2820, 3022, 4622, 3104]
        take = [4502, 3155, 3287] 
        course = 2400
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (True), "test_case_45 error")

    def test_case_46(self):
        # valid input for 2820 
        input = [1300, 2824, 3702, 2270]
        take = [] 
        course = 2820
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (True), "test_case_46 error")

    def test_case_47(self):
        # invalid input for 2820 
        input = [1300]
        take = [2824] 
        course = 2820
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (False), "test_case_47 error")

    def test_case_48(self):
        # valid input for 3104 
        input = [1300, 2824, 3702, 2270]
        take = [] 
        course = 3104
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (True), "test_case_48 error")

    def test_case_49(self):
        # invalid input for 3104 
        input = [1300]
        take = [2270, 2824] 
        course = 3104
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (False), "test_case_49 error")

    def test_case_50(self):
        # invalid input for 3104 
        input = [1300, 2824]
        take = [2270] 
        course = 3104
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (True), "test_case_50 error")

    def test_case_51(self):
        # valid input for 4502 
        input = [1300, 2824, 3702, 2270]
        take = [2400] 
        course = 4502
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (True), "test_case_51 error")

    def test_case_52(self):
        # invalid input for 4502 
        input = [1300, 2824, 3702]
        take = [] 
        course = 4502
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (False), "test_case_52 error")

    def test_case_53(self):
        # valid input for 3403 
        input = [1300, 2824, 3702, 2270, 2400]
        take = [] 
        course = 3403
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (True), "test_case_53 error")

    def test_case_54(self):
        # invalid input for 3403 
        input = [1300, 2824, 3702]
        take = [2400] 
        course = 3403
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (False), "test_case_54 error")

    def test_case_55(self):
        # valid input for 3022 
        input = []
        take = [1300] 
        course = 3022
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (True), "test_case_55 error")

    def test_case_56(self):
        # invalid input for 3022 
        input = []
        take = [] 
        course = 3022
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (False), "test_case_56 error")

    def test_case_57(self):
        # valid input for 3308 co
        input = [1300, 2824]
        take = [2270] 
        course = 3308
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (True), "test_case_57 error")

    def test_case_58(self):
        # valid input for 3308 pre
        input = [1300, 2824, 2270]
        take = [] 
        course = 3308
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (True), "test_case_58 error")

    def test_case_59(self):
        # invalid input for  3308
        input = [1300, 2824]
        take = [] 
        course = 3308
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (False), "test_case_59 error")

    def test_case_60(self):
        # valid input for 3155
        input = [1300, 2824, 2270]
        take = [] 
        course = 3155
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (True), "test_case_60 error")

    def test_case_61(self):
        # invalid input for  3155
        input = [1300, 2824]
        take = [2270] 
        course = 3155
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (False), "test_case_61 error")
    
    def test_case_62(self):
        # valid input for 2270
        input = [1300, 2824]
        take = [] 
        course = 2270
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (True), "test_case_62 error")

    def test_case_63(self):
        # invalid input for  2270
        input = []
        take = [1300] 
        course = 2270
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (False), "test_case_63 error")

    def test_case_64(self):
        # valid input for 3753
        input = [1300, 2824, 2270]
        take = [] 
        course = 3753
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (True), "test_case_64 error")

    def test_case_65(self):
        # invalid input for  3753
        input = [1300, 2824]
        take = [2270] 
        course = 3753
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (False), "test_case_65 error")

    def test_case_66(self):
        # valid input for 4122
        input = [1300, 2824, 2270]
        take = [] 
        course = 4122
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (True), "test_case_66 error")

    def test_case_67(self):
        # valid input for  4122 co 
        input = [1300, 3702]
        take = [2824] 
        course = 4122
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (True), "test_case_67 error")

    def test_case_68(self):
        # invalid input for  4122 co 
        input = []
        take = [1300, 3702] 
        course = 4122
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (False), "test_case_68 error")

    def test_case_69(self):
        # valid input for 4622
        input = [1300, 2270, 3022, 2824, 3104, 2820]
        take = [] 
        course = 4622
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (True), "test_case_69 error")

    def test_case_70(self):
        # invalid input for 4622
        input = [1300, 2270, 3022, 2824, 3104]
        take = [] 
        course = 4622
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (False), "test_case_70 error")

    def test_case_71(self):
        # invalid input for 4622
        input = [1300, 2270, 3022, 2824, 2820]
        take = [] 
        course = 4622
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (False), "test_case_71 error")
    
    def test_case_72(self):
        # invalid input for 4622
        input = [1300, 2270, 3104, 2824, 2820]
        take = [] 
        course = 4622
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (False), "test_case_72 error")

    def test_case_73(self):
        # valid input for 3287
        input = [1300, 2824, 2270]
        take = [] 
        course = 3287
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (True), "test_case_73 error")

    def test_case_74(self):
        # invalid input for  3287
        input = [1300, 2824]
        take = [2270] 
        course = 3287
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (False), "test_case_74 error")

    def test_case_75(self):
        # valid input for 3202
        input = [1300, 2824, 2270, 3022]
        take = [] 
        course = 3202
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (True), "test_case_75 error")

    def test_case_76(self):
        # invalid input for 3202
        input = [1300, 2270, 3022]
        take = [2824] 
        course = 3202
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (False), "test_case_76 error")

    def test_case_77(self):
        # invalid input for 3202
        input = [1300, 2270, 2824]
        take = [3022] 
        course = 3202
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (False), "test_case_77 error")
    
    def test_case_78(self):
        # invalid input for 3202
        input = [1300, 2824, 2270]
        take = [] 
        course = 3202
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (False), "test_case_78 error")

    def test_case_79(self):
        # valid input for 3302
        input = [1300, 2824, 2270, 2820]
        take = [] 
        course = 3302
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (True), "test_case_79 error")

    def test_case_80(self):
        # invalid input for 3302
        input = [1300, 2824, 2270]
        take = [] 
        course = 3302
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (False), "test_case_80 error")

    def test_case_81(self):
        # invalid input for 3302
        input = [1300, 2824, 2820]
        take = [] 
        course = 3302
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (False), "test_case_81 error")
    
    def test_case_82(self):
        # invalid input for 3302
        input = [1300, 2270, 2820]
        take = [2824] 
        course = 3302
        p = cspbAlg.preReqChecker(input, take, course)
        self.assertEqual(p, (False), "test_case_82 error")
    
    def test_case_83(self):
        # testing overload of dontWant 
        input = [1300, 2824, 2270, 3104, 3308, 2400, 3155, 3753] 
        inputHours = 20
        inputElectives = [] 
        dontWant = [3702, 3403, 4502, 2820, 3022, 4122]
        inputSemester = 0
        p = cspbAlg.basicAlg(input, inputHours, inputElectives, inputSemester, dontWant)
        self.assertEqual(p, ([3287, 3702, 4502], 39), "test_case_83 error")

    def test_case_84(self):
        # testing overload of dontWant
        input = [1300, 2824, 2270, 3104, 3308, 2400, 3155, 3753, 3287, 3702] 
        inputHours = 30
        inputElectives = [4622] 
        dontWant = [3702, 3403, 4502, 2820, 3022, 4122]
        inputSemester = 0
        p = cspbAlg.basicAlg(input, inputHours, inputElectives, inputSemester, dontWant)
        self.assertEqual(p, ([3022, 2820], 42), "test_case_84 error")
    
    def test_case_85(self):
        # testing overload of dontWant
        input = [1300, 2824, 2270, 3104, 3308, 2400, 3155, 3753, 3287, 3702, 3022, 2820] 
        inputHours = 30
        inputElectives = [4622] 
        dontWant = [3702, 3403, 4502, 2820, 3022, 4122]
        inputSemester = 1
        p = cspbAlg.basicAlg(input, inputHours, inputElectives, inputSemester, dontWant)
        self.assertEqual(p, ([4622], 45), "test_case_85 error")

    def test_case_86(self):
        # testing overload of dontWant
        input = [1300, 2824, 3702, 2270, 3308, 4122, 3104, 2820, 2400, 4502, 3155, 3287]
        inputHours = 30
        inputElectives = [3022] 
        dontWant = []
        inputSemester = 5
        p = cspbAlg.basicAlg(input, inputHours, inputElectives, inputSemester, dontWant)
        self.assertEqual(p, ([3403], 45), "test_case_86 error")

    

    

if __name__ == '__main__':
    unittest.main() 