# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlCarpAssert(PerlPackage):
    """Carp::Assert - executable comments."""

    homepage = "https://metacpan.org/pod/Carp::Assert"
    url = "https://cpan.metacpan.org/authors/id/Y/YV/YVES/Carp-Assert-0.22.tar.gz"

    version("0.22", sha256="807ea97c6bed76ac2e4969efba7dae48fefeb9f28797f112671b3ac8a49355f7")

    depends_on("perl-extutils-makemaker", type="build")
