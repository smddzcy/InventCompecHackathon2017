#!/usr/bin/python

import sys, os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
import numpy as np
import datetime as dt
import json, itertools

normalization_values = np.asarray([[1.30512529e-01,3.36866455e-01],
                                    [1.27035186e-01,3.33012383e-01],
                                    [1.35834117e-01,3.42612331e-01],
                                    [1.40033982e-01,3.47022284e-01],
                                    [1.44402105e-01,3.51496994e-01],
                                    [1.66503357e-01,3.72531863e-01],
                                    [1.55678725e-01,3.62550493e-01],
                                    [4.01675987e-02,1.96352140e-01],
                                    [3.37506805e-02,1.80586744e-01],
                                    [3.07418221e-02,1.72617388e-01],
                                    [3.04251002e-02,1.71753933e-01],
                                    [3.37077910e-02,1.80475970e-01],
                                    [3.20944887e-02,1.76251050e-01],
                                    [3.29159862e-02,1.78416715e-01],
                                    [3.30809455e-02,1.78847971e-01],
                                    [3.21538741e-02,1.76408624e-01],
                                    [3.15996107e-02,1.74931630e-01],
                                    [3.08309002e-02,1.72859353e-01],
                                    [3.68222233e-02,1.88325110e-01],
                                    [3.08473961e-02,1.72904119e-01],
                                    [2.96695864e-02,1.69674106e-01],
                                    [3.48658056e-02,1.83439857e-01],
                                    [3.17447749e-02,1.75319834e-01],
                                    [3.02238498e-02,1.71202712e-01],
                                    [3.26784448e-02,1.77793599e-01],
                                    [3.34273602e-02,1.79749748e-01],
                                    [3.22429521e-02,1.76644683e-01],
                                    [3.13257782e-02,1.74196653e-01],
                                    [2.99863084e-02,1.70549493e-01],
                                    [3.10453473e-02,1.73440289e-01],
                                    [3.18074595e-02,1.75487165e-01],
                                    [3.36879959e-02,1.80424818e-01],
                                    [3.24079114e-02,1.77080882e-01],
                                    [3.33580772e-02,1.79569808e-01],
                                    [3.94714703e-02,1.94713824e-01],
                                    [3.15303278e-02,1.74746005e-01],
                                    [3.11773148e-02,1.73796691e-01],
                                    [2.02108180e-02,1.40720790e-01],
                                    [1.03825407e-02,1.01364410e-01],
                                    [3.71818347e-03,6.08634421e-02],
                                    [3.29258838e-03,5.72865363e-02],
                                    [2.68223883e-03,5.17208316e-02],
                                    [2.50738193e-03,5.00109485e-02],
                                    [2.73502582e-03,5.22259078e-02],
                                    [3.03195262e-03,5.49796316e-02],
                                    [3.24969895e-03,5.69134290e-02],
                                    [3.45094934e-03,5.86433312e-02],
                                    [3.49713796e-03,5.90331092e-02],
                                    [3.36517049e-03,5.79124003e-02],
                                    [7.17573118e-03,8.44052135e-02],
                                    [2.89338678e-03,5.37123365e-02],
                                    [3.19031359e-03,5.63926900e-02],
                                    [3.47404365e-03,5.88385475e-02],
                                    [3.74787615e-03,6.11050699e-02],
                                    [3.47404365e-03,5.88385475e-02],
                                    [3.27609244e-03,5.71433256e-02],
                                    [3.27609244e-03,5.71433256e-02],
                                    [3.42455585e-03,5.84194168e-02],
                                    [3.49053958e-03,5.89775866e-02],
                                    [3.46744527e-03,5.87828385e-02],
                                    [4.00851190e-03,6.31857874e-02],
                                    [3.68849079e-03,6.06208365e-02],
                                    [2.98906320e-03,5.45905550e-02],
                                    [3.40476073e-03,5.82509084e-02],
                                    [3.35527293e-03,5.78274595e-02],
                                    [3.35197374e-03,5.77991177e-02],
                                    [3.27279326e-03,5.71146398e-02],
                                    [3.28928919e-03,5.72579232e-02],
                                    [3.38826479e-03,5.81101063e-02],
                                    [1.84094621e-03,4.28667368e-02],
                                    [1.72877386e-03,4.15425709e-02],
                                    [1.98611042e-03,4.45215205e-02],
                                    [2.29293479e-03,4.78296691e-02],
                                    [2.82410386e-03,5.30672055e-02],
                                    [2.14117220e-03,4.62232364e-02],
                                    [2.17746326e-03,4.66124652e-02],
                                    [2.12137708e-03,4.60095299e-02],
                                    [1.81785190e-03,4.25975036e-02],
                                    [1.56711371e-03,3.95557564e-02],
                                    [1.77496247e-03,4.20928970e-02],
                                    [1.76176572e-03,4.19364031e-02],
                                    [2.20385675e-03,4.68934938e-02],
                                    [2.58656241e-03,5.07924414e-02],
                                    [2.14447139e-03,4.62587573e-02],
                                    [1.74856898e-03,4.17793189e-02],
                                    [1.44834298e-03,3.80295318e-02],
                                    [1.41865030e-03,3.76382483e-02],
                                    [1.60340476e-03,4.00104218e-02],
                                    [2.05209416e-03,4.52535421e-02],
                                    [2.16096732e-03,4.64359510e-02],
                                    [1.67928606e-03,4.09446706e-02],
                                    [1.39555600e-03,3.73310651e-02],
                                    [1.41865030e-03,3.76382483e-02],
                                    [1.52422428e-03,3.90115498e-02],
                                    [2.32922585e-03,4.82058145e-02],
                                    [1.83434783e-03,4.27899872e-02],
                                    [2.38201283e-03,4.87477061e-02],
                                    [1.94322100e-03,4.40391291e-02],
                                    [1.80465515e-03,4.24428836e-02],
                                    [1.68588443e-03,4.10248976e-02],
                                    [1.67598687e-03,4.09044978e-02],
                                    [1.63639663e-03,4.04192879e-02],
                                    [1.98281124e-03,4.44846007e-02],
                                    [2.36881609e-03,4.86128049e-02],
                                    [1.63309744e-03,4.03785888e-02],
                                    [1.51102753e-03,3.88425582e-02],
                                    [1.45494136e-03,3.81159350e-02],
                                    [1.34606819e-03,3.66641009e-02],
                                    [1.28998202e-03,3.58931465e-02],
                                    [1.80795434e-03,4.24815918e-02],
                                    [2.27973804e-03,4.76921465e-02],
                                    [1.62979825e-03,4.03378484e-02],
                                    [1.31307633e-03,3.62125967e-02],
                                    [1.74197060e-03,4.17005533e-02],
                                    [1.88383563e-03,4.33622739e-02],
                                    [1.25369097e-03,3.53852967e-02],
                                    [1.39555600e-03,3.73310651e-02],
                                    [1.64299500e-03,4.05005626e-02],
                                    [1.84424539e-03,4.29050598e-02],
                                    [1.23719503e-03,3.51520181e-02],
                                    [1.08213325e-03,3.28779902e-02],
                                    [1.28338365e-03,3.58013488e-02],
                                    [2.13787301e-03,4.61876879e-02],
                                    [1.82115109e-03,4.26360704e-02],
                                    [2.10818033e-03,4.58665009e-02],
                                    [1.73537223e-03,4.16216376e-02],
                                    [1.37576087e-03,3.70657275e-02],
                                    [1.47803566e-03,3.84168072e-02],
                                    [1.59350720e-03,3.98869394e-02],
                                    [1.43184705e-03,3.78126548e-02],
                                    [1.55721615e-03,3.94308410e-02],
                                    [1.80465515e-03,4.24428836e-02],
                                    [1.36586331e-03,3.69323399e-02],
                                    [1.16131374e-03,3.40582602e-02],
                                    [1.22069910e-03,3.49171733e-02],
                                    [1.37246169e-03,3.70213187e-02],
                                    [1.48793322e-03,3.85450292e-02],
                                    [1.84094621e-03,4.28667368e-02],
                                    [1.91352832e-03,4.37020220e-02],
                                    [1.63969581e-03,4.04599458e-02],
                                    [1.24709259e-03,3.52921713e-02],
                                    [1.54072021e-03,3.92217592e-02],
                                    [1.41535112e-03,3.75945195e-02],
                                    [1.39225681e-03,3.72869740e-02],
                                    [1.61000313e-03,4.00925308e-02],
                                    [1.74856898e-03,4.17793189e-02],
                                    [1.92672506e-03,4.38521698e-02],
                                    [1.21080154e-03,3.47755014e-02],
                                    [1.42854786e-03,3.77691291e-02],
                                    [1.53742103e-03,3.91798081e-02],
                                    [1.91352832e-03,4.37020220e-02],
                                    [1.83104865e-03,4.27515603e-02],
                                    [1.72547467e-03,4.15029807e-02],
                                    [1.82115109e-03,4.26360704e-02],
                                    [1.53742103e-03,3.91798081e-02],
                                    [1.77496247e-03,4.20928970e-02],
                                    [2.00590554e-03,4.47423947e-02],
                                    [1.47473648e-03,3.83739707e-02],
                                    [2.09168440e-03,4.56870798e-02],
                                    [2.06199172e-03,4.53623182e-02],
                                    [1.93002425e-03,4.38896258e-02],
                                    [1.77496247e-03,4.20928970e-02],
                                    [2.01250392e-03,4.48157756e-02],
                                    [2.22695106e-03,4.71380074e-02],
                                    [2.66574289e-03,5.15619696e-02],
                                    [3.37836723e-03,5.80254588e-02],
                                    [3.41135910e-03,5.83071327e-02],
                                    [2.40510714e-03,4.89828807e-02],
                                    [1.82774946e-03,4.27130986e-02],
                                    [1.64629419e-03,4.05411384e-02],
                                    [1.50772834e-03,3.88001946e-02],
                                    [1.61000313e-03,4.00925308e-02],
                                    [1.74526979e-03,4.17399548e-02],
                                    [1.85414295e-03,4.30198223e-02],
                                    [1.73537223e-03,4.16216376e-02],
                                    [2.22365187e-03,4.71031553e-02],
                                    [1.75846654e-03,4.18971877e-02],
                                    [1.75516735e-03,4.18579352e-02],
                                    [1.60340476e-03,4.00104218e-02],
                                    [1.70897874e-03,4.13044565e-02],
                                    [1.67268768e-03,4.08642851e-02],
                                    [1.54731859e-03,3.93055262e-02],
                                    [1.28338365e-03,3.58013488e-02],
                                    [1.32627307e-03,3.63938741e-02],
                                    [1.39555600e-03,3.73310651e-02],
                                    [2.18406163e-03,4.66828823e-02],
                                    [1.94652018e-03,4.40764250e-02],
                                    [1.81125353e-03,4.25202644e-02],
                                    [1.56381452e-03,3.95141621e-02],
                                    [1.42194949e-03,3.76819260e-02],
                                    [1.85744214e-03,4.30580080e-02],
                                    [1.96301612e-03,4.42624297e-02],
                                    [2.04219660e-03,4.51445017e-02],
                                    [2.13127464e-03,4.61165080e-02],
                                    [2.35232015e-03,4.84436450e-02],
                                    [2.04219660e-03,4.51445017e-02],
                                    [1.91022913e-03,4.36644037e-02],
                                    [2.06199172e-03,4.53623182e-02],
                                    [2.24674618e-03,4.73465765e-02],
                                    [2.07848765e-03,4.55430296e-02],
                                    [2.24344699e-03,4.73118794e-02],
                                    [2.05869253e-03,4.53260887e-02],
                                    [2.06859009e-03,4.54346897e-02],
                                    [2.25994292e-03,4.74851091e-02],
                                    [2.33912341e-03,4.83078866e-02],
                                    [2.19395919e-03,4.67883076e-02],
                                    [2.66904208e-03,5.15937816e-02],
                                    [2.13457383e-03,4.61521118e-02],
                                    [2.36551690e-03,4.85790205e-02],
                                    [2.69213639e-03,5.18159125e-02],
                                    [2.36551690e-03,4.85790205e-02],
                                    [2.19395919e-03,4.67883076e-02],
                                    [1.99930717e-03,4.46688923e-02],
                                    [2.31272991e-03,4.80352078e-02],
                                    [2.04219660e-03,4.51445017e-02],
                                    [2.26654130e-03,4.75542226e-02],
                                    [2.30613154e-03,4.79667937e-02],
                                    [2.17416407e-03,4.65772163e-02],
                                    [2.16096732e-03,4.64359510e-02],
                                    [2.51398030e-03,5.00765435e-02],
                                    [2.31602910e-03,4.80693781e-02],
                                    [2.47439006e-03,4.96816612e-02],
                                    [2.42490226e-03,4.91835553e-02],
                                    [2.53047624e-03,5.02401525e-02],
                                    [1.89703238e-03,4.35136030e-02],
                                    [2.25334455e-03,4.74158938e-02],
                                    [1.81785190e-03,4.25975036e-02],
                                    [1.96301612e-03,4.42624297e-02],
                                    [1.95641774e-03,4.41881225e-02],
                                    [2.17416407e-03,4.65772163e-02],
                                    [2.27643886e-03,4.76577033e-02],
                                    [2.16096732e-03,4.64359510e-02],
                                    [2.21045512e-03,4.69634859e-02],
                                    [2.22695106e-03,4.71380074e-02],
                                    [2.26654130e-03,4.75542226e-02],
                                    [1.03924383e-03,3.22205493e-02],
                                    [1.76836410e-03,4.20147235e-02],
                                    [1.91022913e-03,4.36644037e-02],
                                    [2.09168440e-03,4.56870798e-02],
                                    [2.14447139e-03,4.62587573e-02],
                                    [1.88713482e-03,4.34001560e-02],
                                    [1.85744214e-03,4.30580080e-02],
                                    [2.00260636e-03,4.47056588e-02],
                                    [1.98611042e-03,4.45215205e-02],
                                    [2.14447139e-03,4.62587573e-02],
                                    [1.87723726e-03,4.32864094e-02],
                                    [2.69873476e-03,5.18792019e-02],
                                    [2.51727949e-03,5.01093085e-02],
                                    [2.12797545e-03,4.60808765e-02],
                                    [2.82740305e-03,5.30981058e-02],
                                    [2.27643886e-03,4.76577033e-02],
                                    [2.23025024e-03,4.71728336e-02],
                                    [2.01250392e-03,4.48157756e-02],
                                    [2.33912341e-03,4.83078866e-02],
                                    [2.72182907e-03,5.21001028e-02],
                                    [2.67234127e-03,5.16255737e-02],
                                    [2.47109088e-03,4.96486111e-02],
                                    [2.44469738e-03,4.93834065e-02],
                                    [2.72842744e-03,5.21630437e-02],
                                    [2.61625509e-03,5.10823874e-02],
                                    [2.58986160e-03,5.08247402e-02],
                                    [2.45129576e-03,4.94498423e-02],
                                    [2.58326323e-03,5.07601219e-02],
                                    [2.23354943e-03,4.72076338e-02],
                                    [2.36221771e-03,4.85452123e-02],
                                    [2.50408274e-03,4.99781183e-02],
                                    [2.17416407e-03,4.65772163e-02],
                                    [2.34572178e-03,4.83758139e-02],
                                    [2.21375431e-03,4.69984425e-02],
                                    [2.22365187e-03,4.71031553e-02],
                                    [2.36881609e-03,4.86128049e-02],
                                    [2.44469738e-03,4.93834065e-02],
                                    [2.21375431e-03,4.69984425e-02],
                                    [2.23684862e-03,4.72424081e-02],
                                    [2.60305835e-03,5.09537284e-02],
                                    [3.25299814e-03,5.69422175e-02],
                                    [2.94947295e-03,5.42288997e-02],
                                    [3.32887943e-03,5.76003298e-02],
                                    [3.30578512e-03,5.74008441e-02],
                                    [3.09793636e-03,5.55728274e-02],
                                    [3.01545669e-03,5.48303174e-02],
                                    [3.42125666e-03,5.83913663e-02],
                                    [3.15732172e-03,5.61012748e-02],
                                    [3.91943386e-03,6.24825728e-02],
                                    [4.05140133e-03,6.35215513e-02],
                                    [3.08803880e-03,5.54842574e-02],
                                    [3.47404365e-03,5.88385475e-02],
                                    [3.93263061e-03,6.25872593e-02],
                                    [3.97881922e-03,6.29522694e-02],
                                    [4.38461919e-03,6.60711307e-02],
                                    [3.82375744e-03,6.17182009e-02],
                                    [3.87324525e-03,6.21147584e-02],
                                    [4.02500784e-03,6.33151415e-02],
                                    [3.17381765e-03,5.62471736e-02],
                                    [3.50373633e-03,5.90885789e-02],
                                    [4.36482407e-03,6.59224725e-02],
                                    [4.26254928e-03,6.51489060e-02],
                                    [3.77097046e-03,6.12923342e-02],
                                    [3.71158509e-03,6.08096146e-02],
                                    [4.05470052e-03,6.35473046e-02],
                                    [4.25925009e-03,6.51237966e-02],
                                    [4.58257040e-03,6.75393992e-02],
                                    [4.18336880e-03,6.45435374e-02],
                                    [4.03820458e-03,6.34184318e-02],
                                    [3.10123555e-03,5.56023190e-02],
                                    [5.68779796e-03,7.52027055e-02],
                                    [4.61226308e-03,6.77568455e-02],
                                    [4.03490540e-03,6.33926252e-02],
                                    [4.12728262e-03,6.41112171e-02],
                                    [8.94739447e-03,9.41665471e-02],
                                    [3.91283549e-03,6.24301626e-02],
                                    [4.23615579e-03,6.49477542e-02],
                                    [6.21566784e-03,7.85941048e-02],
                                    [6.77323040e-03,8.20204471e-02],
                                    [4.32193464e-03,6.55992037e-02],
                                    [3.54002738e-03,5.93927234e-02],
                                    [3.78416720e-03,6.13990821e-02],
                                    [3.78416720e-03,6.13990821e-02],
                                    [4.39781594e-03,6.61700473e-02],
                                    [4.27244684e-03,6.52241753e-02],
                                    [4.35492651e-03,6.58480154e-02],
                                    [3.93592979e-03,6.26134031e-02],
                                    [3.06494449e-03,5.52770351e-02],
                                    [3.11773148e-03,5.57495402e-02],
                                    [3.07814124e-03,5.53955439e-02],
                                    [3.04514937e-03,5.50987880e-02],
                                    [3.94252817e-03,6.26656576e-02],
                                    [3.91283549e-03,6.24301626e-02],
                                    [3.45754771e-03,5.86991744e-02],
                                    [3.37506805e-03,5.79972151e-02],
                                    [3.55982250e-03,5.95579564e-02],
                                    [3.21010871e-03,5.65668093e-02],
                                    [2.76801768e-03,5.25390879e-02],
                                    [4.57927121e-03,6.75151945e-02],
                                    [3.81056070e-03,6.16120144e-02],
                                    [3.08473961e-03,5.54547022e-02],
                                    [3.50703552e-03,5.91162940e-02],
                                    [3.43115422e-03,5.84754769e-02],
                                    [4.24275416e-03,6.49981015e-02],
                                    [4.08109401e-03,6.37529504e-02],
                                    [3.71818347e-03,6.08634421e-02],
                                    [3.66539648e-03,6.04314599e-02],
                                    [4.42750862e-03,6.63920612e-02],
                                    [2.94287458e-03,5.41683863e-02],
                                    [3.49053958e-03,5.89775866e-02],
                                    [2.23354943e-03,4.72076338e-02],
                                    [2.86039491e-03,5.34061144e-02],
                                    [5.04115735e-03,7.08219181e-02],
                                    [3.68849079e-03,6.06208365e-02],
                                    [2.80760792e-03,5.29124301e-02],
                                    [2.55027136e-03,5.04357757e-02],
                                    [2.88348922e-03,5.36206556e-02],
                                    [2.60965672e-03,5.10180989e-02],
                                    [3.50373633e-03,5.90885789e-02],
                                    [5.20611669e-03,7.19653600e-02],
                                    [3.48394121e-03,5.89220108e-02],
                                    [3.74127778e-03,6.10514588e-02],
                                    [2.59975916e-03,5.09215123e-02],
                                    [2.55686973e-03,5.05008133e-02],
                                    [3.16062091e-03,5.61304853e-02],
                                    [4.53968097e-03,6.72240453e-02],
                                    [6.11009386e-03,7.79279194e-02],
                                    [3.97552003e-03,6.29262686e-02],
                                    [3.23650220e-03,5.67981272e-02],
                                    [3.04514937e-03,5.50987880e-02],
                                    [3.34867455e-03,5.77707619e-02],
                                    [3.53012982e-03,5.93099318e-02],
                                    [3.72478184e-03,6.09172212e-02],
                                    [4.18336880e-03,6.45435374e-02],
                                    [3.89633955e-03,6.22989413e-02],
                                    [3.48724040e-03,5.89498053e-02],
                                    [3.04514937e-03,5.50987880e-02],
                                    [2.80760792e-03,5.29124301e-02],
                                    [2.91318190e-03,5.38952249e-02],
                                    [2.72512826e-03,5.21315829e-02],
                                    [3.33217862e-03,5.76287706e-02],
                                    [3.96562247e-03,6.28482006e-02],
                                    [3.72148265e-03,6.08903377e-02],
                                    [3.64230217e-03,6.02414791e-02],
                                    [3.42455585e-03,5.84194168e-02],
                                    [3.79406476e-03,6.14790195e-02],
                                    [3.25959651e-03,5.69997504e-02],
                                    [3.47074446e-03,5.88106997e-02],
                                    [3.78746639e-03,6.14257396e-02],
                                    [4.67824681e-03,6.82375323e-02],
                                    [2.80430874e-03,5.28814201e-02],
                                    [2.89008759e-03,5.36817938e-02],
                                    [5.33148579e-03,7.28221192e-02],
                                    [5.20611669e-03,7.19653600e-02],
                                    [3.69178997e-03,6.06478414e-02],
                                    [4.12728262e-03,6.41112171e-02],
                                    [3.45094934e-03,5.86433312e-02],
                                    [3.23650220e-03,5.67981272e-02],
                                    [3.30248594e-03,5.73722888e-02],
                                    [3.49053958e-03,5.89775866e-02],
                                    [3.08473961e-03,5.54547022e-02],
                                    [3.96232329e-03,6.28221560e-02],
                                    [4.05470052e-03,6.35473046e-02],
                                    [3.66209729e-03,6.04043569e-02],
                                    [3.05504693e-03,5.51879844e-02],
                                    [3.24310058e-03,5.68558077e-02],
                                    [3.09463717e-03,5.55433200e-02],
                                    [4.45390211e-03,6.65887743e-02],
                                    [2.28963560e-03,4.77953259e-02],
                                    [1.13551410e-01,3.17265641e-01],
                                    [5.49413570e-02,2.27865759e-01],
                                    [5.13122515e-02,2.20633870e-01],
                                    [4.78283103e-02,2.13402819e-01],
                                    [5.92138038e-02,2.36024425e-01],
                                    [6.57593903e-02,2.47861035e-01],
                                    [6.61288992e-02,2.48507279e-01],
                                    [7.99359958e-02,2.71194086e-01],
                                    [1.23171838e-01,3.28634351e-01],
                                    [1.21258310e-01,3.26427223e-01],
                                    [1.04544630e-01,3.05965766e-01],
                                    [1.12353805e-01,3.15801247e-01],
                                    [1.11458340e+01,7.08089889e+00],
                                    [2.44549598e+02,9.44803919e+01],
                                    [6.92297974e+01,7.00811957e+01],
                                    [4.37737088e+00,3.36479120e+00]])

# Normalize each column in the matrix
def normalize_matrix(matrix):
    for i in range(matrix.shape[1]):
        matrix[:, [i]] -= normalization_values[i, 0]
        std = normalization_values[i, 1]
        if std != 0:
            matrix[:, [i]] /= std
    return matrix

def one_hot(num, num_classes):
    """ Creates a one-hot vector with given num and num_classes """
    return np.eye(num_classes)[num].astype(int)

def flatten(arr):
    return np.array(list(itertools.chain.from_iterable(arr)))

def map_fn(row):
    """ Splits the date column into 4 one-hot boolean vectors """
    result = np.array(row)
    date = dt.datetime.strptime(str(int(row[0])), "%Y%m%d").timetuple()
    res = flatten(np.array([one_hot(date.tm_wday, 7), one_hot(date.tm_mday - 1, 31),
            one_hot(date.tm_yday - 1, 366), one_hot(date.tm_mon - 1, 12), row[1:]]))
    return res

def main(argv):
    # Initialize the variables before restoring
    x = tf.placeholder(tf.float32, [None, 420], name="x")
    y_ = tf.placeholder(tf.float32, name="y_")
    W = tf.Variable(tf.zeros([420,1]), name="W")
    b = tf.Variable(tf.zeros([1]), name="b")
    y = tf.add(tf.matmul(x,W), b)

    with tf.Session() as sess:
        saver = tf.train.Saver()
        # Restore the trained model
        path = os.path.dirname(os.path.realpath(__file__))
        saver.restore(sess, path + "/model_files/multivariate-model.ckpt")
        predict_in = np.array(map(map_fn, np.asarray(json.loads(argv[0]))))
        predict_in = normalize_matrix(predict_in)
        result = sess.run(y, feed_dict={ x: predict_in })
        print(json.dumps(result.tolist()))

if __name__ == "__main__":
   main(sys.argv[1:])
