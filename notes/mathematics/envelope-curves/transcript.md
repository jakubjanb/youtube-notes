---
title: "That weird light at the bottom of a mug — ENVELOPES"
youtube_url: "https://www.youtube.com/watch?v=fJWnA4j0_ho&t=398s"
source_language: "en"
transcript_source: "auto-generated"
---

# Transcript
I've always been fascinated by this. No,

not the cup inside. Okay, it's empty.

See that there at the bottom? That

little bit of light, that shape that it

makes. This could have easily just been

like a single point of light or not

really focus into anything. But instead,

we get this perfect little heart-shaped

curve.

I think this is amazing. It's a highly

underrated facet of reality. Why is it

that shape? And what shape is it

exactly? To answer that, we need to talk

about a person on a sled. Have you ever

played Line Rider? It's a game where you

can draw lines and a little person on a

sled will ride on top of them.

Instead of the usual game where you just

try to make a cool course to sled

through, let's play our own and restrict

ourselves to a goal of going from here

to there while making as smooth and

uniform of a curve as possible and only

using straight lines. How do you think

you might do it? Just connecting these

points with one straight line. obviously

won't cut it. This is far from smooth.

The problem, of course, is these little

discontinuities where two lines connect.

So, obviously, we're going to need more

smaller lines to approximate a smooth

curve. If I just, you know, go for it

and start drawing small pieces towards a

curve. Well, it kind of works, but my

curve shape gets really weird. I sort of

lose track of where I'm going. I end up

going too high or too low or just being

inconsistent. Really, I'm just bad at

eyeballing things. I have bad eyeballs.

Okay. Well, here, let's take one of my

bad curves. What if we were to take each

segment in here and extend it out in

both directions? Well, notice the

extended parts stay underneath the curve

we're making. So, doing this doesn't

actually affect the sled. We end up with

a sort of regular pattern of lines on

the sides. Now, here's the trick. Let's

go the other way. Start with two lines

representing the inbound and outbound

paths. Connect the top of the first to

the bottom of the second. then just

below the first to just above the other

and so on and so forth. And what do you

know? We get a pristine curve, much

smoother and more consistent than when I

freehanded it. Plus, we have easy

control over the incoming and outgoing

directions from the lines we started

with. What's going on here is

surprisingly interesting. It's worth

exploring the maths behind this and how

it relates to the shape we saw in the

coffee cup earlier. We've stumbled into

something called envelopes.

Envelopes. Envelopes. Envelopes.

envelopes. To talk about envelopes,

let's talk about curves. We can

represent a curve implicitly as a

function of x and y. f(x, y)= 0. For

example, a line looks like x + y= 0. A

parabola like y - x^2= 0 and so on.

Next, let's talk about families of

curves. Well, when a mommy curve loves a

daddy curve, uh, a family of curves is

just a set of related curves where each

curve is described by a parameter t. So

like this curve might be t=0 and this

one t= 1.5 and this one t= 3.14.

We can make our implicit function give

an entire family of curves by adding a

parameter t. So f of xyt is equal to x +

y + t= 0. That would be a set of lines.

Plugging in a t gives you a new line in

the family. f ofxy = 0. Here it would

shift up and down. Okay, now we can

really talk about envelopes. The

envelope of a family of curves is itself

a curve which is tangent to a family

member at every point. So we take a

family of curves and we produce a new

curve out of it. Our trick from before

is exactly this. Here the family of

curves are the lines we drew. We start

with one line. Then as t changes we

shift over to the other line. We only

drew a finite number but if we

considered all infinitely many lines we

would see a perfect curve appear. That

curve is the envelope of the set of

lines. I think envelopes are really cool

because it's this really tangible thing.

Like it's right there. That curvy part

you see, that's the envelope. Not every

family of curves has an envelope. This

set of circles, these parallel lines. A

family of curves also doesn't have to be

made out of lines. They could be sort of

wavy things or whatever. You can even

have multiple envelopes for one set of

curves. Okay, now math time. What's

really going on here? Let's zoom in on a

curve from the family. It's got some

parameter t.

Somewhere on this curve, there's a point

that's actually on the envelope. And

that envelope is itself some kind of

smooth function.

How can we find this point on the

envelope knowing our function f ofxyt?

Let's look at two nearby neighboring

curves. Nearby meaning that their

parameters t are similar like 0.5 and

0.51.

In many cases, two nearby curves will

have some place where they intersect.

This certainly isn't always true, for

example, with parallel lines, but like I

said, we don't always have an envelope.

In this case, they do intersect, right

over there. What happens if we chose

curves that were even closer, so the

difference in their parameter was really

small in the limit? As the curves

approach each other, this intersection

settles in on some point. This is how we

define a point in the envelope. We can

do this process for any t We pick two

curves, find their intersection point,

take the limit as the curves approach

each other at t, and we end up with a

point on the envelope. Okay, we have

this intuitive idea, but how can we make

it into something concrete, something we

can calculate? Let's look again at what

we're saying.

intersecting there. If you know

calculus, then you might see what's

about to happen. If not, bear with me.

You already have the crucial intuition.

So, if this t small changes in t result

in small changes in x and y, well, we're

comparing a small change in f ofxyt to a

small change in t. That comparison,

that's a derivative. More specifically,

the partial derivative with respect to t

since we hold xy constant. So when the

partial derivative of f with respect to

t is zero, it means that changes in t

don't change x and y at all, which is to

say that the infinite decimally adjacent

curves are intersecting. The partial

derivative gives us the specific

relationship to describe x, y, and t

where this happens. The math backs us up

on this too. We can take two curves with

parameters t and u, rearrange their

definition, then take the limit as u

approaches t, and we see the definition

of the partial derivative. This is the

mechanism we can use to mathematically

define and calculate the envelope. You

may notice that the partial derivative

expression is underspecified. It is an

expression of t and x and y. So we need

two things. The envelope is the curve

that satisfies both f ofxyt equals 0

which is saying it must be on a member

of the family of curves and the partial

derivative of f with respect to t is

equal to z. As we just arrived, we call

these the envelope conditions. the

conditions needed for a point to be in

the envelope.

You can use these ideas to actually

calculate the specific envelope for a

family of curves. I won't go into math

too too much, but let's lay out how this

would look for our lines from before.

First, we define our family of curves.

Here, it's a bunch of lines whose slope

depends on t. Next, we take the partial

derivative with respect to t. Now, we

apply the envelope conditions. We set

the partial derivative equal to zero and

consider the original definition of the

family. Finally, we just solve for the

curve. For this example, we get the

expression of a rotated parabola. In

fact, this example is exactly equivalent

to a quadratic bezier curve, if you know

what that is. This is itself pretty

cool, but let's keep going. Finally, we

return to the figure at the bottom of

the coffee cup. It may not surprise you

to learn that this too is the envelope

of a family of curves.

Each ray of light traveling in a

straight line is a member of the family.

When rays reflect off the curved wall,

they are reflected in such a way that

certain rays will intersect.

Now, this intersection, it doesn't

itself produce light. Photons pass right

through each other, basically. But you

probably have an intuitive understanding

that rays of light will be brighter when

they converge. Think of a magnifying

glass. It's converging rays from the

sun. So, if we consider nearby rays of

light reflecting off the coffee cup,

they will produce the brightest spot

where they intersect. That's the shape

we see because we most easily see the

brightest part. This is called a costic

reflection of light. And it should be

very clear how this relates to

envelopes. We even have all the tools we

need to calculate what the shape is. We

can use geometry to find what these

reflected lines are and how they relate

to a parameter t. They look like this.

Here, our parameter t is essentially the

angle between the point on the edge of

the light and where it's hitting on the

cup. Now we can apply the envelope

conditions. So taking the partial

derivatives and the original curve, we

now have two equations of lines. Solving

the system of equation gives us these

parametric equations. This function

produces exactly the heart-shaped curve

we saw at the beginning. I think it's

cool that we can use envelopes to find

what this shape is. We use geometry to

set it up, but ultimately we had to use

a little bit of calculus and some

intuitive understanding to really get to

the bottom of what's going on. Envelopes

are a pretty nifty tool. I love that you

can see them appear out of nowhere and

you can use a pretty general method to

compute their exact shape. Thanks for

watching. Now you have all the tools you

need to look at the bottom of a mug.



