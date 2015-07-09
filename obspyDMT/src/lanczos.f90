!=========================================================================================
! copyright:
!     Martin van Driel (Martin@vanDriel.de), 2014
! license:
!     GNU Lesser General Public License, Version 3 [non-commercial/academic use]
!     (http://www.gnu.org/copyleft/lgpl.html)

module lanczos

    use iso_c_binding, only: c_double, c_int
    implicit none
    private

    double precision, parameter   :: pi = 3.1415926535898D0

    public :: lanczos_resamp, lanczos_kern


contains

!-----------------------------------------------------------------------------------------
pure subroutine lanczos_resamp(si, n_in, so, n_out, dt, a) bind(c, name="lanczos_resamp")
    ! lanczos resampling, see http://en.wikipedia.org/wiki/Lanczos_resampling
    real(c_double), intent(in)          :: si(1:n_in)
    integer(c_int), intent(in), value   :: n_in
    real(c_double), intent(out)         :: so(1:n_out)
    integer(c_int), intent(in), value   :: n_out
    real(c_double), intent(in), value   :: dt
    integer(c_int), intent(in), value   :: a

    integer(c_int)    :: i, l, m
    real(c_double)    :: x, kern

    so = 0
    do l=1, n_out
        x = dt * (l - 1)
        do m=-a, a
            i = floor(x) - m + 1
            if (i < 1 .or. i > n_in) cycle
            call lanczos_kern(x - i + 1, a, kern)
            so(l) = so(l) + si(i) * kern
        enddo
    enddo

end subroutine
!-----------------------------------------------------------------------------------------

!-----------------------------------------------------------------------------------------
pure subroutine lanczos_kern(x, a, kern) bind(c, name="lanczos_kern")
    real(c_double), intent(in), value   :: x
    integer(c_int), intent(in), value   :: a
    real(c_double), intent(out)         :: kern

    if (x > -a .and. x < a) then
        kern = sinc(x) * sinc(x / a)
    else
        kern = 0
    endif

end subroutine
!-----------------------------------------------------------------------------------------

!-----------------------------------------------------------------------------------------
pure function sinc(x)
    double precision, intent(in) :: x
    double precision             :: sinc

    if (abs(x) < 1e-10) then
        sinc = 1
    else
        sinc = sin(pi * x) / (pi * x)
    endif

end function
!-----------------------------------------------------------------------------------------

end module lanczos
!=========================================================================================
