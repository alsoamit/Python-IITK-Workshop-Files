
banner = r"""
************************************************************************
*                        STUDENT GRADING SYSTEM                        *
************************************************************************
"""

login_header = banner + r"""
 ______________________________________________________________________
|                                LOGIN                                 |
------------------------------------------------------------------------
"""

home_header = banner + r"""
 ______________________________________________________________________
|                                 HOME                                 |
------------------------------------------------------------------------
|  [A]dd Students  |   [C]ompute GPA    | Compute GPA [N] Assign Grade |
------------------------------------------------------------------------
| [U]pdate Records | [G]enerate Records | [D]isplay Records | [L]ogout |
------------------------------------------------------------------------
site-path: /home{:>55}
"""

add_students_header = banner + r"""
 ______________________________________________________________________
|                             ADD STUDENTS                             |
------------------------------------------------------------------------
|  <-- Go [B]ack  |  [U]pload File   |   [M]anual Entry   |  [L]ogout  |
------------------------------------------------------------------------
site-path: /home/add{:>51}
"""

update_records_header = banner + r"""
 ______________________________________________________________________
|                            UPDATE RECORDS                            |
------------------------------------------------------------------------
|  <-- Go [B]ack  |  [U]pload File  |  Update [M]anually  |  [L]ogout  |
------------------------------------------------------------------------
site-path: /home/update{:>48}
"""

display_records_header = banner + r"""
 ______________________________________________________________________
|                           DISPLAY RECORDS                            |
------------------------------------------------------------------------
| <-- Go [B]ack  |  [S]ingle Record  |  [M]ultiple Records  | [L]ogout |
------------------------------------------------------------------------
site-path: /home/display{:>47}


Note: The latest updates will be visible only after you Generate Records
"""

multiple_records_header = banner + r"""
 ______________________________________________________________________
|                           MULTIPLE RECORDS                           |
------------------------------------------------------------------------
| <-- Go [B]ack  |  [P]revious Entries  |  [N]ext Entries  |  [L]ogout |
------------------------------------------------------------------------
site-path: /home/display/multiple{:>38}

Note: The latest updates will be visible only after you Generate Records
"""
