import math

from manim import *


class CloseLabelDot(VGroup):
    def __init__(self, position=ORIGIN, colour=GREEN, label=0, label_pos=ORIGIN, **kwargs):
        dot = Dot(position, radius=0.03, color=colour)
        super().__init__(dot, Tex(str(label), font_size=20).move_to(label_pos), **kwargs)


# 5 hour intervals on clock
twelfth = TAU / 12
fifth_angle = TAU * (5 / 12)


def point_on_clock(index):
    return Circle(1.05).point_at_angle(twelfth * (3 - index))


class AdditiveDynamics(Scene):

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

        # points and arcs on circle
        count = 5

        dots = [Dot(point_on_clock(i*5), radius=0.05, color=YELLOW) for i in range(count+1)]
        # distance = math.sqrt(point_on_clock(8)[0]**2 + point_on_clock(8)[1]**2)
        arrows = [ArcBetweenPoints(point_on_clock(i*5), point_on_clock(5*(i+1)),
                                   angle=-TAU/4, stroke_width=2, color=YELLOW).add_tip(tip_length=0.1, tip_width=0.1)
                  for i in range(count)]
        mod_texts = [Text(f"({i})5 ≡ {((5*i) % 12)} (mod 12)").move_to(DOWN * 3) for i in range(1, count+1)]

        # 360 degrees

        # infinite group

        # addition in Zn as rotation, additive inverses

        # mod_texts = [Text("(3)5 ≡ 3 (mod 12)").move_to(DOWN * 3) for i in range(multiples)]
        # inverse_texts = [MarkupText(f"Additive inverse of 3 is 9 in Z<sub>12</sub>").move_to(DOWN * 3)
        #                  for i in range(multiples)]

        # animations
        self.wait(1)
        self.play(FadeIn(circle), *[FadeIn(d) for d in hr_dots], run_time=1.5)
        div_text = Text("θ = 150° = 5/12").move_to(DOWN * 3)
        self.add(div_text)
        # subcaption = "θ = 150° = 5/12", subcaption_duration=6)
        self.wait(1)
        self.remove(div_text)
        # additive dynamics up to 5(5) congruent to 1
        self.add(dots[0])
        self.wait(1)
        self.play(Create(arrows[0]), Write(mod_texts[0]), Create(dots[1]))
        self.wait(1)
        for i in range(1, count):
            self.remove(mod_texts[i - 1])
            self.wait(1)
            self.add(dots[i+1])
            self.play(Create(arrows[i]), Write(mod_texts[i]))
            self.play(FadeOut(arrows[i - 1]))
            self.wait(1)
        # additive inverses
        self.remove(mod_texts[count - 1])
        self.play(FadeOut(arrows[count - 1]), *[FadeOut(d) for d in dots])
        two_fives = Arc(radius=1.05, start_angle=clock_angles[3], angle=-fifth_angle*2, stroke_width=2, color=YELLOW)
        self.play(Create(dots[0]), Create(dots[2]), Create(two_fives), Write(mod_texts[1]))
        self.wait(1)
        self.remove(mod_texts[1])
        two_fives_inv = Arc(radius=1.05, start_angle=clock_angles[5], angle=-twelfth*2, stroke_width=2, color=RED)
        inv_text = Text(f"additive inverse of (2)5 ≡ 2 (mod 12)").move_to(DOWN * 3)
        self.play(Create(two_fives_inv), Write(inv_text))
        self.wait(2)
        self.remove(inv_text)
        self.play(FadeOut(dots[2]))
        self.wait(1)
        rotate_text = Text(f"(2)5 ≡ 10 (mod 12) as a rotation").move_to(DOWN * 3)
        self.play(Write(rotate_text))
        self.play(Rotate(dots[0], angle=-fifth_angle*2, about_point=ORIGIN))
        rotate_inv_text = Text(f"-(2)5 ≡ 2 (mod 12) as a rotation").move_to(DOWN * 3)
        self.wait(1)
        self.remove(rotate_text)
        self.play(Write(rotate_inv_text))
        self.play(Rotate(dots[0], angle=-twelfth*2, about_point=ORIGIN))
        self.wait(1)
        self.play(FadeOut(dots[0]), FadeOut(two_fives), FadeOut(two_fives_inv))
        self.remove(rotate_inv_text)
        self.wait(1)
        arith_text_1 = Text(f"(5)5 = (1)5 + 2[(2)5]").move_to(DOWN * 3)
        arith_text_2 = Text(f"(1)5 + 2[(2)5] = (1)5 - 2[-(2)5]").move_to(DOWN * 3)
        arith_text_3 = Text(f"(1)5 - 2[-(2)5] = 5 - 2⋅(2) ≡ 1 (mod 12)").move_to(DOWN * 3)
        one_five = Arc(radius=1.05, start_angle=clock_angles[3], angle=-fifth_angle, stroke_width=2, color=YELLOW)
        sub_inv_arcs = [Arc(radius=1.05, start_angle=clock_angles[(10 + 2*i) % 12], angle=twelfth*2,
                            stroke_width=2, color=RED) for i in range(2)]
        self.play(Write(arith_text_1))
        self.wait(1)
        self.remove(arith_text_1)
        self.play(Write(arith_text_2))
        self.wait(1)
        self.remove(arith_text_2)
        self.play(Write(arith_text_3))
        self.wait(1)
        self.play(Create(dots[0]), Create(one_five))
        self.wait(1)
        self.play(Rotate(dots[0], angle=-fifth_angle, about_point=ORIGIN))
        self.wait(1)
        self.play(FadeOut(one_five))
        self.play(Create(sub_inv_arcs[0]))
        self.play(Rotate(dots[0], angle=2*twelfth, about_point=ORIGIN))
        self.wait(1)
        self.play(FadeOut(sub_inv_arcs[0]))
        self.play(Create(sub_inv_arcs[1]))
        self.play(Rotate(dots[0], angle=2*twelfth, about_point=ORIGIN))
        self.play(FadeOut(sub_inv_arcs[1]))
        self.wait(2)



