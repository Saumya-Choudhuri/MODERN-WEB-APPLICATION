<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" encoding="UTF-8" indent="yes"/>

    <xsl:template match="/library">
        <html>
            <head>
                <title>Book List</title>
                <style>
                    table {
                        width: 60%;
                        border-collapse: collapse;
                        margin: 20px 0;
                        font-size: 18px;
                        text-align: left;
                    }
                    th, td {
                        padding: 10px;
                        border: 1px solid black;
                    }
                    th {
                        background-color: lightpink;
                    }
                </style>
            </head>
            <body>
                <h2>Book List</h2>
                <table>
                    <tr>
                        <th>Title</th>
                        <th>Publisher</th>
                        <th>ISBN</th>
                        <th>Price (₹)</th>
                    </tr>
                    <xsl:for-each select="books/book">
                        <tr>
                            <td><xsl:value-of select="title"/></td>
                            <td><xsl:value-of select="publisher"/></td>
                            <td><xsl:value-of select="isbn"/></td>
                            <td><xsl:value-of select="price"/></td>
                        </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>