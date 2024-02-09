import math

from manim import *


class CloseLabelDot(VGroup):
    def __init__(self, position=ORIGIN, colour=GREEN, label=0, label_pos=ORIGIN, **kwargs):
        dot = Dot(position, radius=0.03, color=colour)
        super().__init__(dot, Tex(str(label), font_size=20).move_to(label_pos), **kwargs)


# divisions of circle
divisions = 45
step_len = 16
angle = TAU / divisions
step = TAU * (step_len / divisions)


def point_on_clock(index):
    return Circle(1.05).point_at_angle(step * index)


class AdditiveDynamics2(Scene):

    def construct(self):
        circle = Circle(1, color=GREY)

        # divided circle
        circle_angles = [n * (TAU / divisions) for n in range(divisions)]
        circle_pts = [circle.point_at_angle(angle=a) for a in circle_angles]
        # labels are positioned on circle with slightly larger radius
        lab_circle = Circle(1.2)
        lab_pts = [lab_circle.point_at_angle(angle=a) for a in circle_angles]
        circle_dots = [CloseLabelDot(position=circle_pts[i], label=i, label_pos=lab_pts[i])
                       for i in range(divisions)]

        # points and arcs on circle
        count = 14

        dots = [Dot(point_on_clock(i * step_len), radius=0.04, color=YELLOW) for i in range(count + 1)]
        # distance = math.sqrt(point_on_clock(8)[0]**2 + point_on_clock(8)[1]**2)
        arrows = [ArcBetweenPoints(point_on_clock(i * step_len), point_on_clock(step_len * (i + 1)),
                                   angle=-TAU / 4, stroke_width=2, color=YELLOW)
                  .add_tip(tip_length=0.01, tip_width=0.01)
                  for i in range(count)]
        mod_texts = [Text(f"({i}){step_len} ≡ {((step_len * i) % divisions)} (mod {divisions})").move_to(DOWN * 3)
                     for i in range(1, count + 1)]

        # 360 degrees

        # infinite group

        # addition in Zn as rotation, additive inverses

        # mod_texts = [Text("(3)5 ≡ 3 (mod 12)").move_to(DOWN * 3) for i in range(multiples)]
        # inverse_texts = [MarkupText(f"Additive inverse of 3 is 9 in Z<sub>12</sub>").move_to(DOWN * 3)
        #                  for i in range(multiples)]

        # animations
        self.wait(1)
        self.play(FadeIn(circle), *[FadeIn(d) for d in circle_dots], run_time=1.5)
        div_text = Text("θ = 128° = 16/45").move_to(DOWN * 3)
        self.add(div_text)
        # subcaption = "θ = 150° = 5/12", subcaption_duration=6)
        self.wait(1)
        self.remove(div_text)
        self.add(dots[0])
        for i in range(count):
            self.remove(mod_texts[i - 1])
            self.wait(1)
            self.play(Create(arrows[i]), Write(mod_texts[i]), Create(dots[i + 1]))
            self.remove(arrows[i - 1])
            self.wait(1)
        self.wait(2)
