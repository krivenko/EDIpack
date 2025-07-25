MODULE ED_DIAG
  !:synopsis: Fock space ED-Lanczos diagonalization routines
  USE ED_INPUT_VARS
  USE ED_VARS_GLOBAL
  USE ED_EIGENSPACE
  USE ED_DIAG_NORMAL
  USE ED_DIAG_SUPERC
  USE ED_DIAG_NONSU2
  !
  implicit none
  private

  public  :: diagonalize_impurity

contains

  subroutine  diagonalize_impurity()
    !
    ! Call the correct impurity diagonalization procedure according to the value of :f:var:`ed_mode`.
    !
    ! * :f:var:`normal` : :f:func:`diagonalize_impurity_normal`
    ! * :f:var:`superc` : :f:func:`diagonalize_impurity_superc`
    ! * :f:var:`nonsu2` : :f:func:`diagonalize_impurity_nonsu2`
    !
#ifdef _DEBUG
    write(Logfile,"(A)")"DEBUG diagonalize_impurity: Start digonalization"
#endif
    !
    write(LOGfile,"(A)")"Diagonalize impurity problem:"
    select case(ed_mode)
    case default  ;STOP "diagonalize_impurity error: ed_mode "//trim(ed_mode)//" not valid"
    case("normal");call diagonalize_impurity_normal()
    case("superc");call diagonalize_impurity_superc()
    case("nonsu2");call diagonalize_impurity_nonsu2()
    end select
#ifdef _DEBUG
    write(Logfile,"(A)")""
#endif
    call es_return_evals(state_list,ed_evals)
    !
  end subroutine diagonalize_impurity

end MODULE ED_DIAG
