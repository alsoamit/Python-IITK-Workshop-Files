import sys, os
sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from Util.pyt import run
#from P35_solution import main
from P35 import main

#### Test Cases Begin #######

def testcase1() -> None:
    inp='''3'''
    out='''_A_\n_A_B_\n_A_B_C_'''
    res=run(main,inp)
    assert(res==out)

def testcase2() -> None:
    inp='''4'''
    out='''_A_\n_A_B_\n_A_B_C_\n_A_B_C_D_'''
    res=run(main,inp)
    assert(res==out)

def testcase3() -> None:
    inp='''1'''
    out='''_A_'''
    res=run(main,inp)
    assert(res==out)

def testcase4() -> None:
    inp='''26'''
    out='''_A_\n_A_B_\n_A_B_C_\n_A_B_C_D_\n_A_B_C_D_E_\n_A_B_C_D_E_F_\n_A_B_C_D_E_F_G_\n_A_B_C_D_E_F_G_H_\n_A_B_C_D_E_F_G_H_I_\n_A_B_C_D_E_F_G_H_I_J_\n_A_B_C_D_E_F_G_H_I_J_K_\n_A_B_C_D_E_F_G_H_I_J_K_L_\n_A_B_C_D_E_F_G_H_I_J_K_L_M_\n_A_B_C_D_E_F_G_H_I_J_K_L_M_N_\n_A_B_C_D_E_F_G_H_I_J_K_L_M_N_O_\n_A_B_C_D_E_F_G_H_I_J_K_L_M_N_O_P_\n_A_B_C_D_E_F_G_H_I_J_K_L_M_N_O_P_Q_\n_A_B_C_D_E_F_G_H_I_J_K_L_M_N_O_P_Q_R_\n_A_B_C_D_E_F_G_H_I_J_K_L_M_N_O_P_Q_R_S_\n_A_B_C_D_E_F_G_H_I_J_K_L_M_N_O_P_Q_R_S_T_\n_A_B_C_D_E_F_G_H_I_J_K_L_M_N_O_P_Q_R_S_T_U_\n_A_B_C_D_E_F_G_H_I_J_K_L_M_N_O_P_Q_R_S_T_U_V_\n_A_B_C_D_E_F_G_H_I_J_K_L_M_N_O_P_Q_R_S_T_U_V_W_\n_A_B_C_D_E_F_G_H_I_J_K_L_M_N_O_P_Q_R_S_T_U_V_W_X_\n_A_B_C_D_E_F_G_H_I_J_K_L_M_N_O_P_Q_R_S_T_U_V_W_X_Y_\n_A_B_C_D_E_F_G_H_I_J_K_L_M_N_O_P_Q_R_S_T_U_V_W_X_Y_Z_'''
    res=run(main,inp)
    assert(res==out)

def testcase5() -> None:
    inp='''13'''
    out='''_A_\n_A_B_\n_A_B_C_\n_A_B_C_D_\n_A_B_C_D_E_\n_A_B_C_D_E_F_\n_A_B_C_D_E_F_G_\n_A_B_C_D_E_F_G_H_\n_A_B_C_D_E_F_G_H_I_\n_A_B_C_D_E_F_G_H_I_J_\n_A_B_C_D_E_F_G_H_I_J_K_\n_A_B_C_D_E_F_G_H_I_J_K_L_\n_A_B_C_D_E_F_G_H_I_J_K_L_M_'''
    res=run(main,inp)
    assert(res==out)

def testcase6() -> None:
    inp='''20'''
    out='''_A_\n_A_B_\n_A_B_C_\n_A_B_C_D_\n_A_B_C_D_E_\n_A_B_C_D_E_F_\n_A_B_C_D_E_F_G_\n_A_B_C_D_E_F_G_H_\n_A_B_C_D_E_F_G_H_I_\n_A_B_C_D_E_F_G_H_I_J_\n_A_B_C_D_E_F_G_H_I_J_K_\n_A_B_C_D_E_F_G_H_I_J_K_L_\n_A_B_C_D_E_F_G_H_I_J_K_L_M_\n_A_B_C_D_E_F_G_H_I_J_K_L_M_N_\n_A_B_C_D_E_F_G_H_I_J_K_L_M_N_O_\n_A_B_C_D_E_F_G_H_I_J_K_L_M_N_O_P_\n_A_B_C_D_E_F_G_H_I_J_K_L_M_N_O_P_Q_\n_A_B_C_D_E_F_G_H_I_J_K_L_M_N_O_P_Q_R_\n_A_B_C_D_E_F_G_H_I_J_K_L_M_N_O_P_Q_R_S_\n_A_B_C_D_E_F_G_H_I_J_K_L_M_N_O_P_Q_R_S_T_'''
    res=run(main,inp)
    assert(res==out)
