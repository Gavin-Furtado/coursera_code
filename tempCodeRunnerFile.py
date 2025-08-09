p.array([t1_b,
                   t2_b,
                   t3_b]).T
print(BT_est)
NT = np.array([t1_n,
               t2_n,
               t3_n]).T

BN_est = BT_est @ NT.T