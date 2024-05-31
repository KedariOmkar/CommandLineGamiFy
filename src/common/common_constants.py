import sys
import os
import time
import traceback
import psutil
import humanize
from babel.numbers import format_currency



class Variables:

    # This is the main path of the folder in which it is stored

    main_path = "W:\\Builds\\Python\\GAMIFYGOALS\\gamifygoals\\"
    path = sys.path.append(f"{main_path}")

    # Faces
    entrepeneur_screen = f"{main_path}src\\screen\\faces\\entrepreneur.py"
    techgenius_screen = f"{main_path}src\\screen\\faces\\techgenius.py"
    superhuman_screen = f"{main_path}src\\screen\\faces\\superhuman.py"
    
    # Screens
    home_screen = f"{main_path}src\\screen\\home.py"
    task_screen = f"{main_path}src\\screen\\tasks.py"
    character_screen = f"{main_path}src\\screen\\character.py"
    stats_screen = f"{main_path}src\\screen\\stats.py"
    matrix_screen = f"{main_path}src\\screen\\matrix.py"
    setting_screen = f"{main_path}src\\screen\\setting.py"
    store_screen = f"{main_path}src\\screen\\store.py"

    # game variables to use on behalf of the real variables
    core_goal = "GBM"
    time_variable = "ROAD COVERED"
    mission_variable = "CHECKPOINTS"
    skill_variable = "WEAPONS"
    money_variable = "CASH"
    agent_variable = "AGENTS CHOPPED"

    # game variables measures
    time_measure = "km"
    mission_measure = "done"
    skill_measure = "acq"
    money_measure = "Cr"
    agent_measure = "heads"

    # game targets
    target_time = 142500
    target_mission = 312500
    target_agents_kill = 25000
    reward_money = 10000000

    # game targets for a day
    target_time_day = 1140
    target_mission_day = 2500
    target_agents_kill_day = 2500
    target_cash_day = 2500

    # routine
    routine_a = "3:00 am : SH : Getup -> Scan -> Wash Face -> Drink Water -> Brush -> Report"
    routine_b = "3:30 am : SH : Warmup -> Intense BW -> Weights -> Mma Workouts -> Cool Down"
    routine_c = "4:10 am : SH : Bath -> Aarti -> Breakfast"
    routine_d = "4:30 am : SH : Plan -> Prioritize -> Tasks -> Targets "
    routine_e = "5:00 am : TG : LANG"
    routine_f = "6:00 am : TG : LANG"
    routine_g = "7:00 am : TG : LANG"
    routine_h = "8:00 am : TG : DSA"
    routine_i = "9:00 am : TG : DSA"
    routine_j = "10:00 am :TG : DSA"
    routine_k = "11:00 am : EN : SOFTS "
    routine_l = "12:00 pm : EN : SOFTS"
    routine_m = "12:30 pm : EN : SOFTS"
    routine_n = "1:00 pm : EN :  BUSI"
    routine_o = "2:00 pm : EN : BUSI"
    routine_p = "3:00 pm : EN : BUSI"
    routine_q = "4:00 pm : TG : TECH"
    routine_r = "5:00 pm : TG : TOOLS"
    routine_s = "6:00 pm : TG : BUILD"
    routine_t = "7:00 pm : TG : BUILD"
    routine_u = "8:00 pm : TG : SUB"
    routine_v = "9:00 pm : TG : SUB"
    routine_w = "9:30 pm : TG : Recall"
    routine_x = "10:00 pm : SH : Analyse Reports -> See Mistakes -> Improvise -> Report"
    routine_y = "10:30 pm : SH : Wash Face -> Apply Gel -> Recall Day -> Meditation"
    routine_z = "11:00 pm : SH : Sleep -> Rest -> Hyper Processing -> Hare Krishna"

    # Paths of the gbm
    paths = [f'{main_path}',
             f'{main_path}\\common',
             f'{main_path}\\database',
             f'{main_path}\\media',
             f'{main_path}\\screen',
             f'{main_path}\\test_frames',
             f'{main_path}\\venv\\lib\\site-packages',
             f'{main_path}src']


""" Creating object of Variables """
var = Variables()