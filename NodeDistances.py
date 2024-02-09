import math
import random

from manim import *

PHI = golden = (1 + 5 ** 0.5) / 2


def polar_curve(i):
    r = 1 + math.sqrt(i) * 0.25
    vector = [r * math.cos(i * TAU / PI), r * math.sin(i * TAU / PI), 0]
    return vector


class NodeDistances(Scene):

    # parametric function for growth spiral (with angle as parameter)

    def construct(self):
        # meristem
        meristem = Circle(1, color=BLUE)

        # nodes
        count = 40
        polar_angles = [i * TAU / PHI for i in range(count)]
        polar_dists = [1 + math.sqrt(i) * 0.25 for i in range(count)]
        x_vals = [math.cos(polar_angles[i]) * polar_dists[i] for i in range(count)]
        y_vals = [math.sin(polar_angles[i]) * polar_dists[i] for i in range(count)]
        # points = [Point(location=[x_vals[i], y_vals[i],0] for i in range(count))]
        nodes = [Dot(point=[x_vals[i], y_vals[i], 0], radius=0.03, color=YELLOW)
                 for i in range(count)]

        # polar distance lines
        origin = Point(location=[0, 0, 0])
        # endpoints lie on the unit circle
        endpoints = [meristem.point_at_angle(angle=a) for a in polar_angles]
        lines = [Line(origin, nodes[i], stroke_width=1) for i in range(count)]

        # distance between nodes
        indices = [[10, 31], [10, 17]]
        dist_lines = [Line(nodes[pair[0]], nodes[pair[1]], stroke_width=1) for pair in indices]

        # generative spiral
        plane = PolarPlane(radius_max=polar_dists[count - 1]).add_coordinates()
        # spiral_func = ParametricFunction(polar_curve, t_range=[0,50], fill_opacity=0,
        # stroke_width=2, fill_color=GREEN)
        spiral_func = ParametricFunction(lambda t: plane.polar_to_point(1 + math.sqrt(t/(TAU/PHI)) * 0.25, t),
                                         t_range=[0, 40*(TAU/PHI)], color=GREEN, stroke_width=1)

        # animation
        self.wait(1)
        self.play(FadeIn(meristem), *[FadeIn(n) for n in nodes], run_time=1.5)
        self.wait(1)
        cosine_law = Tex(r"$a^2 = b^2 + c^2 - 2bc\cos A$").move_to(DOWN * 3)
        self.add(cosine_law)
        # distance between arbitrary nodes
        self.wait(2)
        self.play(*[Flash(nodes[node_index]) for node_index in indices[0]])
        self.remove(cosine_law)
        dist_formula = Tex(r"$d = \sqrt{d_1^2 + d_2^2 - 2d_1d_2\cos (\alpha - \beta)}$").move_to(DOWN * 3)
        #self.add(dist_formula)
        self.play(Write(dist_formula))
        self.wait(1)
        self.play(*[FadeIn(lines[node]) for node in indices[0]])
        self.wait(1)
        self.play(FadeIn(dist_lines[0]))
        self.wait(2)
        self.play(FadeOut(lines[indices[0][0]]), FadeOut(lines[indices[0][1]]), FadeOut(dist_lines[0]))
        self.wait(1)
        self.play(*[Flash(nodes[node_index]) for node_index in indices[1]])
        self.wait(1)
        self.play(*[FadeIn(lines[node]) for node in indices[1]])
        self.wait(1)
        self.play(FadeIn(dist_lines[1]))
        self.wait(2)
        self.play(FadeOut(lines[indices[1][0]]), FadeOut(lines[indices[1][1]]), FadeOut(dist_lines[1]))
        self.wait(1)
        self.remove(dist_formula)
        self.play(Write(plane))
        self.play(Create(spiral_func), run_time=5)
        self.wait(2)
