<p>Here we have bike stuff</p>

<div class="table">
    <div class="tableheader">
        <div class="tablecell">Greetings</div>
        <div class="tablecell">For you</div>
    </div>
    <div class="tablerow">
        <div class="tablecell">Hello</div>
        <div class="tablecell">There</div>
    </div>
</div>

<style>
    .table {
        display: table;
        border: 1px solid #ccc;
        border-collapse: collapse;
    }
    .tablerow {
        display: table-row;
    }
    .tablecell {
        display: table-cell;
        padding: 8px;
        border: 1px solid #ccc;
        text-align: center;
    }
    .tableheader > .tablecell {
        font-weight: 500;
        color: #a86;
        border-bottom: 1px solid #555;
    }
    .tableheader {
        display: table-header-group;
    }
</style>