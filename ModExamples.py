import math

from manim import *


class CloseLabelDot(VGroup):
    def __init__(self, position=ORIGIN, colour=GREEN, label=0, label_pos=ORIGIN, **kwargs):
        dot = Dot(position, radius=0.05, color=colour)
        super().__init__(dot, Tex(str(label), font_size=20).move_to(label_pos), **kwargs)


class ModExamples(Scene):

    def construct(self):
        circle = Circle(1, color=GREY)

        # clock
        divisions = 12
        clock_angles = [n * (TAU / divisions) for n in range(divisions)]
        hr_pts = [circle.point_at_angle(angle=a) for a in clock_angles]
        # labels are positioned on circle with slightly larger radius
        lab_circle = Circle(1.2)
        lab_pts = [lab_circle.point_at_angle(angle=a) for a in clock_angles]
        hr_dots = [CloseLabelDot(position=hr_pts[i], label=(3 - i) % divisions, label_pos=lab_pts[i])
                   for i in range(divisions)]

        # 5 hour intervals on clock
        fifth_angle = TAU * (5 / 12)

        dots = [Dot(Circle(1.05).point_at_angle(clock_angles[3] - i * fifth_angle), radius=0.03, color=YELLOW)
                for i in range(4)]
        dots[3].color = RED
        arcs = [Arc(radius=1.05, start_angle=clock_angles[3] - i * fifth_angle, angle=-fifth_angle,
                    color=YELLOW, stroke_width=2).add_tip() for i in range(3)]
        arcs[2] = Arc(radius=1.075, start_angle=clock_angles[3] - 2 * fifth_angle, angle=-fifth_angle,
                      color=RED, stroke_width=2)
        sect = Sector(outer_radius=1, inner_radius=0, color=BLUE,
                      start_angle=clock_angles[3] - fifth_angle, angle=fifth_angle, fill_opacity=0.2)
        line1_begin = Line(ORIGIN, hr_pts[3], color=YELLOW, stroke_width=1)
        line1_end = Line(ORIGIN, hr_pts[10], color=YELLOW, stroke_width=1)

        inv_arc = Arc(radius=1.075, start_angle=clock_angles[0], angle=-TAU * (3 / 4),
                      color=RED, stroke_width=2)

        # 360 degrees

        # infinite group

        # addition in Zn as rotation, additive inverses
        multiples = 5
        # mod_texts = [Text("(3)5 ≡ 3 (mod 12)").move_to(DOWN * 3) for i in range(multiples)]
        # inverse_texts = [MarkupText(f"Additive inverse of 3 is 9 in Z<sub>12</sub>").move_to(DOWN * 3)
        #                  for i in range(multiples)]

        # animations
        self.wait(1)
        self.play(FadeIn(circle), *[FadeIn(d) for d in hr_dots], run_time=1.5)
        div_text = Text("θ = 150° = 5/12").move_to(DOWN * 3)
        self.add(div_text)
        # subcaption = "θ = 150° = 5/12", subcaption_duration=6)
        self.wait(2)
        self.add(dots[0])
        self.remove(div_text)
        self.wait(1)
        self.play(Create(line1_begin), Create(arcs[0]), Create(sect), Create(line1_end))
        self.add(dots[1])
        self.wait(1)
        self.play(FadeOut(line1_begin), FadeOut(line1_end), FadeOut(sect))
        self.wait(1)
        inverse_1 = MarkupText(f"Additive inverse of 3 is 9 in Z<sub>12</sub>").move_to(DOWN * 3)
        self.play(Create(arcs[1]))
        self.add(dots[2])
        self.wait(1)
        self.play(Create(arcs[2]))
        mod_text = Text("(3)5 ≡ 3 (mod 12)").move_to(DOWN * 3)
        # subcaption="(3)5 ≡ 3 (mod 12)", subcaption_duration=2)
        self.add(mod_text)
        self.add(dots[3])
        self.wait(1)
        self.play(*[FadeOut(arcs[i]) for i in range(3)])
        self.remove(mod_text)
        self.wait(2)
        inverse_text = MarkupText(f"Additive inverse of 3 is 9 in Z<sub>12</sub>").move_to(DOWN * 3)
        self.add(inverse_text)
        self.play(FadeIn(inv_arc), runtime=1)
        self.play(*[Rotate(dot, angle=-TAU * (3 / 4), about_point=ORIGIN) for dot in dots])
        self.play(FadeOut(inv_arc), runtime=0.5)
        self.wait(2)
