class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy:
            return t != 1

        minimum_diagonally_step = min(abs(fx-sx), abs(fy-sy))
        req_steps = minimum_diagonally_step
        if minimum_diagonally_step == abs(fy-sy):
            if sx < fx:
                sx += minimum_diagonally_step
            else:
                fx += minimum_diagonally_step
            req_steps += abs(fx-sx)
        else:
            if sy < fy:
                sy += minimum_diagonally_step
            else:
                fy += minimum_diagonally_step
            req_steps += abs(fy-sy)

        return req_steps <= t