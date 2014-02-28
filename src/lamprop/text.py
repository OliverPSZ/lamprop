# vim:fileencoding=utf-8
# Copyright © 2011-2014 R.F. Smith <rsmith@xs4all.nl>. All rights reserved.
# $Date$
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY AUTHOR AND CONTRIBUTORS ``AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL AUTHOR OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.

"""Text output routines for lamprop."""

from __future__ import print_function

__version__ = '$Revision$'[11:-2]


def out(lam, eng, mat):
    """Plain text main output function."""
    if eng:
        _engprop(lam)
    if mat:
        _matrices(lam, not eng)
    print('')


def _engprop(l):
    """Prints the engineering properties as a plain text table."""
    print("Generated by lamprop {0}".format(__version__))
    print("laminate: {0}".format(l.name))
    s = "thickness: {0:.2f} mm, density: {1:4.2f} g/cm³"
    print(s.format(l.thickness, l.density))
    s = "fiber volume fraction: {0:.1f}%, fiber weight fraction: {1:.1f}%"
    print(s.format(l.vf*100, l.wf*100))
    s = "laminate weight: {0:.0f} g/m², resin consumption: {1:.0f} g/m²"
    print(s.format(l.weight+l.rc, l.rc))
    print("num weight angle   vf fiber")
    for ln, la in enumerate(l.layers):
        s = "{0:3} {1:6g} {2:5g} {3:4g} {4}"
        print(s.format(ln+1, la.weight, la.angle, la.vf, la.fiber.name))
    print("E_x  = {0:.0f} MPa".format(l.Ex))
    print("E_y  = {0:.0f} MPa".format(l.Ey))
    print("G_xy = {0:.0f} MPa".format(l.Gxy))
    print("ν_xy = {0:7.5f}".format(l.Vxy))
    print("ν_yx = {0:7.5f}".format(l.Vyx))
    txt = "α_x = {0:9.4g} K⁻¹, α_y = {1:9.4g} K⁻¹"
    print(txt.format(l.cte_x, l.cte_y))


def _matrices(l, printheader):
    """Prints the ABD and abd matrices as plain text."""
    if printheader is True:
        print("Generated by lamprop {1}".format(__version__))
        print("laminate: {0}".format(l.name))
    print("ABD matrix:")
    matstr = "|{:6.0f} {:6.0f} {:6.0f} {:6.0f} {:6.0f} {:6.0f}|"
    for n in range(6):
        print(matstr.format(l.ABD[n, 0], l.ABD[n, 1], l.ABD[n, 2],
                            l.ABD[n, 3], l.ABD[n, 4], l.ABD[n, 5]))
    matstr = "|{:10g} {:10g} {:10g} {:10g} {:10g} {:10g}|"
    print("abd matrix:")
    for n in range(6):
        print(matstr.format(l.abd[n, 0], l.abd[n, 1], l.abd[n, 2],
                            l.abd[n, 3], l.abd[n, 4], l.abd[n, 5]))
