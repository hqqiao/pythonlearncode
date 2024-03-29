# -*- coding:utf-8 -*-
# Filename: viterbi.py
# Author：hankcs
'''
HMM（隐马尔可夫模型）是用来描述隐含未知参数的统计模型，
举一个经典的例子：一个东京的朋友每天根据天气{下雨，天晴}决定当天的活动{公园散步,购物,清理房间}中的一种，
我每天只能在twitter上看到她发的推“啊，我前天公园散步、昨天购物、今天清理房间了！”，
那么我可以根据她发的推特推断东京这三天的天气。在这个例子里，显状态是活动，隐状态是天气。
'''
# Date: 2014-05-13 下午8:51
#状态 
states = ('Rainy', 'Sunny')
#观测值 
observations = ('walk', 'shop', 'clean')
#初始概率 
start_probability = {'Rainy': 0.6, 'Sunny': 0.4}
#转移概率 
transition_probability = {
    'Rainy' : {'Rainy': 0.7, 'Sunny': 0.3},
    'Sunny' : {'Rainy': 0.4, 'Sunny': 0.6},
    }
#发射概率 
emission_probability = {
    'Rainy' : {'walk': 0.1, 'shop': 0.4, 'clean': 0.5},
    'Sunny' : {'walk': 0.6, 'shop': 0.3, 'clean': 0.1},
}

 
# 打印路径概率表
def print_dptable(V):
    
    print ("    ")
    for i in range(len(V)): print ("%7d" % i),
    print
 
    for y in V[0].keys():
        print ("%.5s: " % y),
        for t in range(len(V)):
            print ("%.7s" % ("%f" % V[t][y])),
        print
 
 
def viterbi(obs, states, start_p, trans_p, emit_p):
    """
    任何一个HMM都可以通过下列五元组来描述：
    :param obs:观测序列
    :param states:隐状态
    :param start_p:初始概率（隐状态）
    :param trans_p:转移概率（隐状态）
    :param emit_p: 发射概率（隐状态表现为显状态的概率）
    :return:
    """
    # 路径概率表 V[时间][隐状态] = 概率
    V = [{}]
    # 一个中间变量，代表当前状态是哪个隐状态
    path = {}
 
    # 初始化初始状态 (t == 0)
    for y in states:
        V[0][y] = start_p[y] * emit_p[y][obs[0]]
        path[y] = [y]
 
    # 对 t > 0 跑一遍维特比算法
    for t in range(1, len(obs)):
        V.append({})
        newpath = {}
 
        for y in states:
            # 概率 隐状态 =    前状态是y0的概率 * y0转移到y的概率 * y表现为当前状态的概率
            (prob, state) = max([(V[t - 1][y0] * trans_p[y0][y] * emit_p[y][obs[t]], y0) for y0 in states])
            # 记录最大概率
            V[t][y] = prob
            # 记录路径
            newpath[y] = path[state] + [y]
 
        # 不需要保留旧路径
        path = newpath
 
    print_dptable(V)
    (prob, state) = max([(V[len(obs) - 1][y], y) for y in states])
    return (prob, path[state])
 
#样例输出查看 
def example():
    return viterbi(observations,
                   states,
                   start_probability,
                   transition_probability,
                   emission_probability)
 
 
print (example())