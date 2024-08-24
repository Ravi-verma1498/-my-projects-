 
import math
import numpy as np

def solve_cubic(a, b, c, d):
    coeffs = [a, b, c, d]
    roots = np.roots(coeffs)
    return roots


with open("C:\\Users\\manav\\Desktop\\RAVI\\test.txt", 'r') as f:
    num_test_cases = int(f.readline())
    with open("output.txt", 'w') as output_file:  # Open the output file
        for i in range(num_test_cases):
            t, P, m = map(float, f.readline().split())

            Tc = 304.1
            Pc = 73.9
            Vc = 56.97
            Tcw = 647.096
            Pcw = 220.64
            R = 83.14
            w = 0.228
            mi = 0.37464 + 1.54226 * w - 0.26992 * w * w
            T = t + 273.15

            ai = 0.457236 * (R * R * Tc * Tc / Pc) * (1 + mi * (1 - (T / Tc) ** 0.5)) ** 2
            bi = 0.077796 * R * Tc / Pc

            A = ai * P / (R * T) ** 2
            B = bi * P / (R * T)

            a1 = 1
            a2 = B - 1
            a3 = A - 2 * B - 3 * B ** 2
            a4 = -(A * B - B * B - B ** 3)
            d1 = 1 + math.sqrt(2)
            d2 = 1 - math.sqrt(2)

            r1, r2, r3 = solve_cubic(a1, a2, a3, a4)
            r = [r1, r2, r3]
            if r1.imag == 0 and r2.imag == 0:

                Zg = round(max(r1, r2, r3), 4)
                Zl = round(min(r1, r2, r3, ), 4)

                k = (Zl + d1 * B) * (Zg + d2 * B) / (Zl + d2 * B) * (Zg + d1 * B)

                ln = math.log(k)
                delG = Zg - Zl + math.log((Zl - B) / (Zg - B)) - A * ln / B * (d1 - d2)
                if delG > 0:
                    Z = Zl
                else:
                    Z = Zg

            else:
                for i in r:
                    if i.imag == 0:
                        Z = i

            lnphi = (Z - 1) - math.log(Z - B) - (A * math.log((Z + d2 * B) / (Z + d1 * B))) / (B * (d2 - d1))
            phi = math.exp(lnphi)
            eta = -0.114535
            tau = -5.279063
            beta = 6.187967
            M = 18.18

            Vo = (1 + 18.1597 * t * 10 ** -3) / (0.9998 + 18.2249 * t * 10 ** -3 - 7.92228 * t * t * 10 ** -6 - 55.4485 * (
                        t ** 3) * 10 ** -9 + 149.7562 * (t ** 4) * 10 ** -12 - 393.2952 * (t ** 5) * 10 ** -15)

            B1 = 19654.32 + 147.037 * t - 2.2155 * t ** 2 + 1.0478 * (t ** 3) * 10 ** -2 - 2.2789 * (t ** 4) * 10 ** -5

            A1 = 3.2891 - 2.391 * t * (10 ** -3) + 2.8446 * (t ** 2) * 10 ** -4 - 2.82 * (t ** 3) * 10 ** -6 + 8.477 * (
                        t ** 4) * 10 ** -9

            A2 = 6.245 * 10 ** -5 - 3.913 * t * 10 ** -6 - 3.499 * t * t * 10 ** -8 + 7.942 * (
                        t ** 3) * 10 ** -10 - 3.299 * (t ** 4) * 10 ** -12

            rho = (Vo - Vo * P / (B1 + A1 * P + A2 * P * P)) ** -1

            lnp = Tcw * (-7.8595178 * (1 - T / Tcw) + 1.8440825 * (1 - T / Tcw) ** 1.5 - 11.786649 * (
                        1 - T / Tcw) ** 3 + 22.680741 * (1 - T / Tcw) ** 3.5 - 15.9618719 * (
                                     1 - T / Tcw) ** 4 + 1.8012250 * (1 - T / Tcw) ** 7.5) / T

            Ps = Pcw * math.exp(lnp)

            fw = Ps * math.exp(18.0152 * (P - Ps) / (rho * R * T))

            delB = tau + beta * (((10 ** 3) / T) ** 0.5)

            lnhi = (1 - eta) * math.log(fw) + eta * math.log(R * T * rho / M) + 2 * rho * delB

            hi = math.exp(lnhi)

            lemma = -0.0652869 + (1.6790636 * 10 ** -4) * T + 40.838951 / T + (-3.9266518 * 10 ** -2) * P / T + (
                        2.1157167 * 10 ** -2) * P / (630 - T) + (6.5486487 * 10 ** -6) * T * math.log(P)

            eps = (-1.144624 * 10 ** -2) + (2.8274958 * 10 ** -5) * T + (1.3980876 * 10 ** -2) * P / T + (
                        -1.4349005 * 10 ** -2) * P / (630 - T)

            lngamma = 2 * m * lemma + 2 * m * m * eps

            gamma = math.exp(lngamma)

            ki = hi * gamma / (P * phi)

            t = T - 273

            logkw = -2.209 + (3.097 * 10 ** -2) * t - (1.098 * 10 ** -4) * t ** 2 + (2.048 * 10 ** -7) * t ** 3
            kow = 10 ** (logkw)
            kw = kow * math.exp((P - 1) * 18.18 / (R * T)) / (fw * P)
            yw = (1 - 1 / ki) / (1 / kw - 1 / ki)

            yi = 1
            yn = yi / (1 + yw)
            x = yn / ki

            
            output_file.write(f"Fugacity coefficient for CO2 (phi) = {phi}\n")
            output_file.write(f"Equilibrium constant for H2O (kw) = {kw}\n")
            output_file.write(f"Vapor phase mole fraction of H2O (y) = {yw}\n")
            output_file.write(f"Henry's coefficient for CO2 (h) = {hi} bar\n")
            output_file.write(f"Liquid phase mole fraction of CO2 (x) = {x}\n\n")



    





