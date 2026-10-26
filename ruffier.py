txt_index = "Your Ruffier Index: "
txt_workheart = "Cardiac performance: "
txt_nodata = "no data for this age"
txt_res = []
txt_res.append("Dangerous \nU gotta check up w the doctor dude")
txt_res.append("Meh \nGood but u should still see the doctor")
txt_res.append("Norm \nUr goood (probably)")
txt_res.append("Ur more then alright \nBetter be safe then sorry")
txt_res.append("Damn.\nStill check up cause why not")

def ruffier_index(P1, P2, P3):
    return (4 * (P1+P2+P3) - 200) / 10

def neud_level (age):
    norm_age = (min(age, 15) - 7) // 2
    result = 21 - norm_age * 1.5
    return result

def ruffier_result(r_index, level):
    if r_index >=:
        return 0
    level = level - 4
        if r_index >= level:
            return 1
    level = level - 5
        if r_index >= level:
            return2
    level = level - 5.5
        if r_index >= level:
            return 3
        return 4

def test(P1, P2, P3, age):
    if age < 7:
        return (txt_index + "0", txt_nodata)
    else:
        ruff_index = ruffier_index(P1, P2, P3)
        result = txt_res[ruffier_result(ruff_index, neud_level(age))]
        res = txt_index + str(ruff_index) + '\n' + txt_workheart + result
        return res











txt_instruction = '''
This app allows us to \n carry out an initial diagnostic of your health \n using a Ruffier test.
A Ruffier test is a stress test\n intended to evaluate the efficiency of the heart during physical strain.\n
The user calculates their pulse frequency over 15 seconds.\n
Then the user does 30 squats over the course of 45 seconds.\n
After the end of the strain, the pulse is calculated again: \n the number of pulsations after the first 15 seconds, 30 seconds of rest,\n and the number of pulsations over the last 15 seconds.\n'''
 
txt_test1 = '''Measure your pulse for 15 seconds.\n
Write your results in the corresponding fields.'''
 
txt_test2 = '''Do 30 squats in 45 seconds.\n
Press the button “Start” to launch the squat counter.
Squat at the speed of the counter.'''
 
txt_test3 = '''Measure your pulse twice within the next minute:\n
during the first 15 seconds, and then during the last 15 seconds of the minute.\n
Write your results in the corresponding fields.'''
 
txt_sits = 'Do 30 squats in 45 seconds.'
 
