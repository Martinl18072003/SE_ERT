class design_structure_matrix():

    def general_dsm(subsystems):
        dsm,row = [],[]
        for i in range(len(subsystems)):
            for j in range(len(subsystems)):
                if i != j: 
                    print(f"Is there a (0:none, 1:physical, 2:mass, 3:energy, 4:information) connection from {subsystems[j]} to {subsystems[i]}?  ",end="")
                    row.append(int(input()))
                else: row.append(-1)
            dsm.append(row)
            row = []
        return dsm
    
    def generate_general_dsm(dsm,subsystems):
        from reportlab.lib import colors
        from reportlab.lib.pagesizes import letter
        from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
        from reportlab.lib.units import inch
        from reportlab.lib.styles import ParagraphStyle

        doc = SimpleDocTemplate("general_design_structure_matrix.pdf", pagesize=letter)
        board_size,cell_size = len(subsystems),60

        data = []
        style = ParagraphStyle(name='Normal',fontName = 'Helvetica',fontSize=17,leftIndent = 18,)
        header_row,sep_row = [Paragraph("")],[Paragraph("")]
        for col_num in range(board_size):
            header_row.append(Paragraph(subsystems[col_num],style))
            sep_row.append("")
        data.append(header_row),data.append(sep_row)
        style = ParagraphStyle(name='Normal',fontName = 'Helvetica',fontSize=14,leftIndent = 0,)

        for i in range(board_size):
            row = [Paragraph(subsystems[i],style)]
            for j in range(board_size):
                if dsm[i][j]==-1: color1, color2, color3, color4 = colors.grey,colors.grey,colors.grey,colors.grey
                elif dsm[i][j]==0: color1, color2, color3, color4 = colors.white,colors.white,colors.white,colors.white
                elif dsm[i][j]==1: color1, color2, color3, color4 = colors.black,colors.white,colors.white,colors.white
                elif dsm[i][j]==2: color1, color2, color3, color4 = colors.white,colors.red,colors.white,colors.white
                elif dsm[i][j]==3: color1, color2, color3, color4 = colors.white,colors.white,colors.green,colors.white
                elif dsm[i][j]==4: color1, color2, color3, color4 = colors.white,colors.white,colors.white,colors.blue
                elif dsm[i][j]==12: color1, color2, color3, color4 = colors.black,colors.red,colors.white,colors.white
                elif dsm[i][j]==13: color1, color2, color3, color4 = colors.black,colors.white,colors.green,colors.white
                elif dsm[i][j]==14: color1, color2, color3, color4 = colors.black,colors.white,colors.white,colors.blue
                elif dsm[i][j]==23: color1, color2, color3, color4 = colors.white,colors.red,colors.green,colors.white
                elif dsm[i][j]==24: color1, color2, color3, color4 = colors.white,colors.red,colors.white,colors.blue
                elif dsm[i][j]==34: color1, color2, color3, color4 = colors.white,colors.white,colors.green,colors.blue
                elif dsm[i][j]==123: color1, color2, color3, color4 = colors.black,colors.red,colors.green,colors.white
                elif dsm[i][j]==124: color1, color2, color3, color4 = colors.black,colors.red,colors.white,colors.blue
                elif dsm[i][j]==134: color1, color2, color3, color4 = colors.black,colors.white,colors.green,colors.blue
                elif dsm[i][j]==234: color1, color2, color3, color4 = colors.white,colors.red,colors.green,colors.blue
                cell = Table([["", ""], ["", ""]], colWidths=[cell_size / 2] * 2, rowHeights=[cell_size / 2] * 2, style=[
                    ('BACKGROUND', (0, 0), (0, 0), color1),('BACKGROUND', (1, 0), (1, 0), color2),('BACKGROUND', (0, 1), (0, 1), color3),
                    ('BACKGROUND', (1, 1), (1, 1), color4),('GRID', (0, 0), (-1, -1), 2, colors.black)])
                row.append(cell)
            data.append(row)

        table = Table(data)
        table.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),('ALIGN', (0, 0), (-1, -1), 'CENTER')]))
        doc.build([table])
    
    def save_dsm(subsystems,dsm,title):
        import csv
        dsm.insert(0,subsystems)
        with open(title+".csv", 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(dsm)

