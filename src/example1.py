import turbodinwriter as tw

pdf = tw.DINA4()

# starting with page 1, not 0
pdf.page(1).text(2, 10, 'NO WARRANTY')
pdf.build('output.pdf')
