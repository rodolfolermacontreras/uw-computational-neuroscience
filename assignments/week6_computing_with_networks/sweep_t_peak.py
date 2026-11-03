"""
Week 6 quiz Q6/Q7: sweep t_peak from 0.5 ms to 10 ms (step 0.5 ms) for the
alpha-synapse integrate-and-fire neuron in alpha_neuron.py, and count output
spikes for each value, using the same fixed random input spike train
(np.random.seed(0)) as the course script.
"""
import numpy as np
from numpy import concatenate as cc


def run_alpha_neuron(t_peak, h=1.0, t_max=200, seed=0):
    tstop = int(t_max / h)
    ref = 0
    np.random.seed(seed)
    thr = 0.9
    spike_train = np.random.rand(tstop) > thr

    t_a = 100
    g_peak = 0.05
    const = g_peak / (t_peak * np.exp(-1))
    t_vec = np.arange(0, t_a + h, h)
    alpha_func = const * t_vec * (np.exp(-t_vec / t_peak))

    C = 0.5
    R = 40
    g_ad = 0
    G_inc = 1 / h
    tau_ad = 2

    E_leak = -60
    E_syn = 0
    V_th = -40
    V_spike = 50
    ref_max = 4 / h
    t_list = np.array([], dtype=int)
    V = E_leak
    spike_count = 0

    for t in range(tstop):
        if spike_train[t]:
            t_list = cc([t_list, [1]])

        g_syn = np.sum(alpha_func[t_list]) if t_list.size else 0.0
        I_syn = g_syn * (E_syn - V)

        if np.any(t_list):
            t_list = t_list + 1
            if t_list.size and t_list[0] == t_a:
                t_list = t_list[1:]

        if not ref:
            V = V + h * (-((V - E_leak) * (1 + R * g_ad) / (R * C)) + (I_syn / C))
            g_ad = g_ad + h * (-g_ad / tau_ad)
        else:
            ref -= 1
            V = V_th - 10
            g_ad = 0

        if (V > V_th) and not ref:
            V = V_spike
            ref = ref_max
            g_ad = g_ad + G_inc
            spike_count += 1

    return spike_count


if __name__ == "__main__":
    results = []
    for tp10 in range(5, 101, 5):  # 0.5 to 10.0 ms in steps of 0.5 ms
        t_peak = tp10 / 10.0
        sc = run_alpha_neuron(t_peak)
        results.append((t_peak, sc))
        print(f"t_peak={t_peak:.1f} ms -> spike_count={sc}")

    scs = np.array([r[1] for r in results])
    print("\nSuccessive differences in spike count:", np.diff(scs))
    print("Sum of increase, first half (0.5-5.0ms):", scs[9] - scs[0])
    print("Sum of increase, second half (5.0-10.0ms):", scs[-1] - scs[9])
